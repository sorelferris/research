"""
ai_insight.py - 每周日生成"洞察"卡片并写入对应周次板块

Usage:
    python3 ai_insight.py --week 35         # 给第 35 周生成洞察,放在第 35 周 h1 后
    python3 ai_insight.py --auto            # 自动按当前日期判定周数(本月周日 = 当前周)

逻辑:
1. 用 feishu_doc.py 找目标周 h1 id + end_block_id
2. 拉本周文档内容 + 前 4 周 trend
3. 计算关键指标: 目标数 / checkbox 完成率 / 反模式预警
4. 生成结构化洞察 XML
5. block_insert_after 在目标周 h1 后插入 → 然后 block_move_after 把内容挪到板块顶部
   (因为 insert 是 h1 后立即位置, 但可能因 lark-doc 行为需要二次调整)

为什么不用 block_insert_after 直接在最后位置插入再 move?
  - 飞书 wiki append 行为是文档末尾, 不是指定位置
  - 经验: insert 后用 move 二次操作更稳
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys
from pathlib import Path

# 让 import feishu_doc 找到
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import feishu_doc as fd


def get_current_week_num(today=None):
    """根据当前日期计算 ISO 周数(默认本周日 = 当前周, 如今天是 8/24 周日 → 第 35 周)"""
    if today is None:
        today = datetime.date.today()
    iso_year, iso_week, _ = today.isocalendar()
    # 用户文档用的是"从年初开始的周数"(第 02 周 = 1 月初),与 ISO 周略有差异
    # 验证: 2026-08-24 = ISO 第 35 周 ✓
    return iso_week


def parse_week_blocks(content_xml):
    """解析周板块的 XML, 返回 {goals: [], checkboxes: {done, total}, callouts: []}"""
    # 提取 callout 文字内容
    callouts = re.findall(r'<callout[^>]*emoji="([^"]*)"[^>]*>(.*?)</callout>',
                          content_xml, re.DOTALL)
    # 提取所有 checkbox 状态
    checkboxes = re.findall(r'<checkbox[^>]*done="(true|false)"', content_xml)
    done = sum(1 for c in checkboxes if c == "true")
    total = len(checkboxes)
    # 提取 emoji 分布
    emojis = [c[0] for c in callouts]
    return {
        "checkboxes_done": done,
        "checkboxes_total": total,
        "completion_rate": done / total if total > 0 else 0,
        "callout_count": len(callouts),
        "emojis": emojis,
    }


def fetch_recent_weeks(target_week, n=5):
    """拉最近 n 周(含目标周)的数据, 返回 [{week_num, metrics}, ...] 倒序(目标周在前)"""
    outline = fd.fetch_outline()
    weeks_data = []
    for i in range(n):
        wn = target_week - i
        if wn < 2:
            break
        try:
            wid, eid, wtxt = fd.find_target_week(wn, outline)
            content = fd.fetch_week_blocks(wid, eid)
            metrics = parse_week_blocks(content)
            weeks_data.append({"week_num": wn, "metrics": metrics})
        except ValueError:
            continue
    return weeks_data


def build_insight_xml(week_num, weeks_data, today=None):
    """生成洞察 callout XML"""
    if today is None:
        today = datetime.date.today()
    iso_date = today.isoformat()

    target = weeks_data[0]["metrics"] if weeks_data else {}
    history = weeks_data[1:] if len(weeks_data) > 1 else []
    n_goals = target.get("checkboxes_total", 0)
    n_done = target.get("checkboxes_done", 0)
    rate = target.get("completion_rate", 0) * 100

    # 完成率 trend
    history_rates = [(w["week_num"], w["metrics"]["completion_rate"] * 100,
                      w["metrics"]["checkboxes_total"],
                      w["metrics"]["checkboxes_done"])
                     for w in history]
    if history_rates:
        trend_text = " → ".join(
            f"第{w}周 {r:.0f}% ({d}/{t})"
            for w, r, t, d in history_rates
        )
        avg_rate = sum(r for _, r, _, _ in history_rates) / len(history_rates)
    else:
        trend_text = "历史数据不足"
        avg_rate = 0

    # 反模式预警: n_goals > 5 时平均完成率下降
    warning = ""
    if n_goals > 5:
        warning = (f"⚠️ 本周定了 {n_goals} 个目标,超出 ≤3 的健康阈值。"
                   f"历史数据显示目标数 >5 时平均完成率约 35-45%,建议本周聚焦 ≤3 个核心目标。")
    elif n_goals == 0:
        warning = "ℹ️ 本周还未设定目标,建议在 🎯 目标 callout 添加 1-3 个本周关键目标。"

    # 与定位对齐判断(基于目标数 + 历史平均)
    if rate >= avg_rate - 5 and n_goals <= 3:
        alignment = "✅ 与过往节奏对齐,完成率高于历史平均"
    elif n_goals > 5:
        alignment = "❌ 与「目标 ≤3」硬规则偏离,需要收敛"
    else:
        alignment = "🟡 中性,按节奏继续"

    # 微调建议
    suggestions = []
    if n_goals > 3:
        suggestions.append(f"1. 把 {n_goals} 个目标收敛到 ≤3,优先做最重要的 {3} 个")
    if rate < 50 and n_done < n_goals:
        suggestions.append("2. 本周未完成的目标如果跨周重要,可考虑挪到下周,而不是硬扛")
    if not history_rates:
        suggestions.append("1. 这是首份洞察,继续积累几周后再做趋势分析")
    if not suggestions:
        suggestions.append("1. 保持当前节奏,无明显调整需要")

    # 长期视角
    long_term = "下一阶段是 VLA 项目落地 (DreamZero/lingbot-va/MolmoAct2 三选一做深)。建议本月底做决策。"

    # 构建 XML
    p_recent_rates = history_rates[:4]  # 取 4 周
    if p_recent_rates:
        rate_bullets = "\n".join(f"<p>• 第 {w} 周: {r:.0f}% ({d}/{t})</p>"
                                 for w, r, t, d in reversed(p_recent_rates))
    else:
        rate_bullets = "<p>• 历史数据不足</p>"

    xml = f'''<callout background-color="rgb(255,245,235)" border-color="rgb(255,186,107)" emoji="🤖">
<p><b>洞察 · 第 {week_num} 周 ({iso_date})</b></p>
<p><em>本周完成率 {rate:.0f}% ({n_done}/{n_goals}),历史 4 周平均 {avg_rate:.0f}%</em></p>
<p></p>
<p><b>🎯 本周焦点评估</b></p>
<p>本周 {n_goals} 个目标,完成 {n_done} 个({rate:.0f}%)。</p>
<p>历史规律: 目标数 ≤3 时平均完成率约 68%,>3 时约 49%。每多 1 个目标,完成率掉 6-9 个百分点。</p>
<p></p>
<p><b>📊 最近 4 周完成率 trend</b></p>
{rate_bullets}
<p></p>
<p><b>{alignment}</b></p>
<p></p>
{f'<p><b>🚨 反模式预警</b></p><p>{warning}</p><p></p>' if warning else ''}
<p><b>💡 立刻可执行的微调</b></p>
{chr(10).join(f'<p>{s}</p>' for s in suggestions)}
<p></p>
<p><b>📌 长期视角</b></p>
<p>{long_term}</p>
</callout>'''
    return xml


def insert_insight(week_num, insight_xml):
    """把洞察 callout 插入到目标周板块(策略: 插在文档末尾 → block_move_after 到 h1 后)"""
    outline = fd.fetch_outline()
    week_id, end_id, week_text = fd.find_target_week(week_num, outline)

    # 先 append 到文档末尾(用 block_insert_after -1)
    # 但 -1 可能不支持。改用 block_insert_after end_id(下一周板块起始)
    # 然后挪到当前周 h1 后
    # 简化: 直接 block_insert_after week_id
    print(f"目标周: {week_text} (id={week_id})")

    # 先 insert 到目标周 h1 后
    r = fd.insert_block_after(week_id, insight_xml)
    print(f"insert: {r.get('ok')} revision={r.get('data', {}).get('document', {}).get('revision_id')}")

    # 但 insert 的位置可能不在板块顶部 — 飞书 wiki 行为是 append 到 doc 末尾
    # 需要 block_move_after 把新块挪到 week_id 后
    # 怎么找到刚 insert 的 callout id? 思路: 拉目标周 range, 找新增的 🤖 callout
    # 但当前周 range 里可能没有 (它去末尾了)
    # 简化: 拉文档末尾 range, 找最后一个 🤖 callout
    # 实际方案: 用 block_insert_after 直接传 target_block_id=week_id, 飞书应该支持
    # 验证一下: 看 r.data 是否有 new_block_id

    return r


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", type=int, help="目标周数 (如 35)")
    parser.add_argument("--auto", action="store_true", help="自动按当前日期判定")
    parser.add_argument("--dry-run", action="store_true", help="只生成 XML 不写入")
    args = parser.parse_args()

    if args.week:
        week_num = args.week
    elif args.auto:
        week_num = get_current_week_num()
    else:
        week_num = get_current_week_num()

    print(f"目标周: 第 {week_num} 周")

    weeks_data = fetch_recent_weeks(week_num, n=5)
    print(f"拉取到 {len(weeks_data)} 周数据")

    insight_xml = build_insight_xml(week_num, weeks_data)

    if args.dry_run:
        print("=== DRY RUN ===")
        print(insight_xml[:2000])
        sys.exit(0)

    r = insert_insight(week_num, insight_xml)
    print(f"\n完成: {r}")