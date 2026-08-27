"""
feishu_doc.py - 飞书文档操作的 lark-cli wrapper
封装: fetch (带 ids), block_insert_after, block_move_after, block_delete
所有操作走 subprocess + lark-cli,无第三方依赖。
"""
import json
import subprocess
import os
import sys
from pathlib import Path

# lark-cli 路径(从 memory 已知: nvm 装)
LARK_CLI = "/home/sorel/.nvm/versions/node/v20.20.2/bin/lark-cli"

# 默认代理(从 memory)
PROXY = "http://192.168.31.31:7890"

DOC_URL = "https://my.feishu.cn/wiki/R4uew012AicUhtkFg2LcJqZfnFc"


def _run(args, timeout=60):
    """执行 lark-cli, 自动加代理 + PATH"""
    env = os.environ.copy()
    env["HTTP_PROXY"] = PROXY
    env["HTTPS_PROXY"] = PROXY
    # 确保 PATH 含 nvm bin(terminal 工具的子进程不 source bashrc)
    env["PATH"] = "/home/sorel/.nvm/versions/node/v20.20.2/bin:" + env.get("PATH", "")
    r = subprocess.run([LARK_CLI] + args, capture_output=True, text=True,
                       timeout=timeout, env=env)
    if r.returncode != 0:
        raise RuntimeError(f"lark-cli failed: {r.stderr[:500]}")
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return {"ok": False, "raw": r.stdout}


def fetch_outline(doc=DOC_URL):
    """拉文档 outline, 返回 [{week_id, week_text}, ...] 列表"""
    out = _run([
        "docs", "+fetch",
        "--doc", doc,
        "--detail", "with-ids", "--scope", "outline",
        "--max-depth", "1"
    ])
    if not out.get("ok"):
        raise RuntimeError(f"fetch failed: {out}")
    import re
    content = out["data"]["document"]["content"]
    h1s = re.findall(r'<h1[^>]*id="([^"]+)">([^<]+)</h1>', content)
    return [{"id": h[0], "text": h[1]} for h in h1s]


def fetch_week_blocks(week_id, end_block_id, doc=DOC_URL):
    """拉一个周板块的全部顶级块(从 week_id 到 end_block_id 不含 end)"""
    out = _run([
        "docs", "+fetch",
        "--doc", doc,
        "--detail", "with-ids",
        "--scope", "range",
        "--start-block-id", week_id,
        "--end-block-id", end_block_id,
        "--context-after", "0", "--context-before", "0"
    ])
    if not out.get("ok"):
        raise RuntimeError(f"fetch range failed: {out}")
    return out["data"]["document"]["content"]


def find_target_week(target_week_num, outline=None):
    """根据周数(如 35)找到对应 h1 id。

    返回: (week_id, end_block_id, week_text)
    end_block_id 是下一周的 h1 id(用于 fetch_week_blocks),如果没有下一周则为 -1。
    """
    if outline is None:
        outline = fetch_outline()
    # outline 顺序是文档顺序: 倒序, 第 35 周在 第 34 周 之前
    weeks = []
    for item in outline:
        text = item["text"].strip()
        m = None
        if text.startswith("第 ") and " 周" in text:
            try:
                num = int(text.replace("第 ", "").replace(" 周", "").strip())
                weeks.append({"num": num, "id": item["id"], "text": text})
            except ValueError:
                pass
    target = None
    for w in weeks:
        if w["num"] == target_week_num:
            target = w
            break
    if not target:
        raise ValueError(f"Week {target_week_num} not found in outline")
    # 找下一周(按周数 num+1) — 但文档是倒序, 所以「下一周板块」(更早的) = num-1
    next_week = None
    for w in weeks:
        if w["num"] == target_week_num - 1:
            next_week = w
            break
    end_id = next_week["id"] if next_week else "-1"
    return target["id"], end_id, target["text"]


def insert_block_after(target_block_id, content_xml, doc=DOC_URL):
    """在 target_block_id 后面插入新块 (XML 格式)"""
    # 写 content 到临时文件, 用 @file 传(1.0.89 wiki 上 v2 str_replace 路径有问题)
    # 但 block_insert_after 用 stdin - 也可
    out = _run([
        "docs", "+update", "--api-version", "v2",
        "--command", "block_insert_after",
        "--doc", doc,
        "--block-id", target_block_id,
        "--content", content_xml,
        "--doc-format", "xml"
    ])
    if not out.get("ok"):
        raise RuntimeError(f"insert failed: {out}")
    return out


def move_block_after(target_block_id, src_block_ids, doc=DOC_URL):
    """把 src_block_ids 列表中的块挪到 target_block_id 后面"""
    if isinstance(src_block_ids, str):
        src_block_ids = [src_block_ids]
    out = _run([
        "docs", "+update", "--api-version", "v2",
        "--command", "block_move_after",
        "--doc", doc,
        "--block-id", target_block_id,
        "--src-block-ids", ",".join(src_block_ids)
    ])
    if not out.get("ok"):
        raise RuntimeError(f"move failed: {out}")
    return out


def delete_block(block_id, doc=DOC_URL):
    """删除一个块"""
    out = _run([
        "docs", "+update", "--api-version", "v2",
        "--command", "block_delete",
        "--doc", doc,
        "--block-id", block_id
    ])
    if not out.get("ok"):
        raise RuntimeError(f"delete failed: {out}")
    return out


def str_replace(pattern, replacement, doc=DOC_URL):
    """inline text 替换"""
    out = _run([
        "docs", "+update", "--api-version", "v2",
        "--command", "str_replace",
        "--doc", doc,
        "--pattern", pattern,
        "--content", replacement
    ])
    if not out.get("ok"):
        raise RuntimeError(f"str_replace failed: {out}")
    return out


if __name__ == "__main__":
    # 简单自测
    print("=== outline (h1 only) ===")
    outline = fetch_outline()
    for h in outline[:5]:
        print(f"  {h['text']}  id={h['id']}")
    print(f"  ... total {len(outline)} h1 blocks")
    print()
    print("=== find_target_week(34) ===")
    wid, eid, txt = find_target_week(34)
    print(f"  week_text={txt}, week_id={wid}, next_h1_id={eid}")