#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_timeline.py — generate the chronological TIMELINE edition.

Single command, single source of truth. Reads:
  * README.md / README.zh-CN.md      -> curated, annotated, topic-tagged picks
  * tools/data/thebrainlab-snapshot.md -> comprehensive conference index (2021-2026),
                                          courtesy of TheBrainLab/Awesome-Spiking-Neural-Networks
De-duplicates the index against the curated picks, then writes:
  * TIMELINE.md         (English)
  * TIMELINE.zh-CN.md   (中文)

Every year shows curated picks first (with a one-line "why it matters" and a topic
tag linking back to the thematic Hub), then a collapsible index of the remaining
papers for that year. Run from the repo root:  python tools/build_timeline.py
"""
import re, io, os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAPSHOT = os.path.join(ROOT, 'tools', 'data', 'thebrainlab-snapshot.md')

# section number -> (emoji, EN label, ZH label, EN anchor, ZH anchor)
# ZH anchors are GitHub slugs of the Chinese headings in README.zh-CN.md.
SECTION_TAGS = {
    1: ("🧩", "Foundations", "基础与编码", "#1--foundations--neural-coding", "#1--基础与神经编码"),
    2: ("🔬", "Neuron Models", "神经元模型", "#2--neuron-models", "#2--神经元模型"),
    3: ("🎓", "Training", "训练方法", "#3--training-methods", "#3--训练方法"),
    4: ("🏗️", "Architectures", "网络结构", "#4--architectures", "#4--网络架构"),
    5: ("🤖", "Spiking LLMs", "脉冲大模型", "#5--spiking-large-models--llms", "#5--脉冲大模型与-llm"),
    6: ("⚙️", "Hardware", "神经形态硬件", "#6--neuromorphic-hardware", "#6--神经形态硬件"),
    7: ("🚀", "Applications", "应用", "#7--applications", "#7--应用"),
    8: ("🔋", "Efficiency & Robustness", "能效与鲁棒", "#8--energy-robustness--security", "#8--能耗鲁棒性与安全"),
    9: ("🧬", "Theory & Neuroscience", "理论与神经科学", "#9--theory--neuroscience", "#9--理论与神经科学"),
}
SKIP_SECTIONS = {10, 11, 12, 13}

# era buckets: (start, end, EN title, ZH title)
ERAS = [
    (2023, 2100, "Spiking Transformers & Large Models", "脉冲 Transformer 与大模型时代"),
    (2018, 2022, "The Deep-SNN Era — Surrogate Gradients Go Deep", "深度脉冲网络时代 — 代理梯度走向深层"),
    (2010, 2017, "Neuromorphic Silicon & Early Deep SNNs", "神经形态芯片与早期深度脉冲网络"),
    (0,    2009, "Foundations — From Neurons to Learning Rules", "奠基时代 — 从神经元到学习法则"),
]

ENTRY_RE = re.compile(r'^- (?P<body>.*\S)\s*$')
ANNOT_RE = re.compile(r'^\s+> (?P<txt>.*\S)\s*$')
SEC_RE   = re.compile(r'^### (?P<num>\d+) · (?P<name>.+?)\s*$')
YEARHDR  = re.compile(r'^### (?P<y>\d{4})\s*$')
BOLD_RE  = re.compile(r'\*\*(?P<v>[^*]+)\*\*')
YEAR_RE  = re.compile(r'\b(?:19|20)\d{2}\b')


# ---------------------------------------------------------------- Hub parsing
def parse_hub(path):
    with io.open(path, encoding='utf-8') as f:
        lines = f.read().split('\n')
    entries, cur_sec, i, n = [], None, 0, len(lines)
    while i < n:
        line = lines[i]
        m = SEC_RE.match(line)
        if m:
            cur_sec = int(m.group('num')); i += 1; continue
        if cur_sec in SKIP_SECTIONS or cur_sec is None:
            i += 1; continue
        em = ENTRY_RE.match(line)
        if em and not line.startswith('- ['):
            body = em.group('body')
            year = None
            for bm in BOLD_RE.finditer(body):
                y = YEAR_RE.search(bm.group('v'))
                if y: year = int(y.group(0))
            if year is None:
                i += 1; continue
            annot, j = [], i + 1
            while j < n:
                am = ANNOT_RE.match(lines[j])
                if am: annot.append(am.group('txt')); j += 1
                else: break
            entries.append(dict(section=cur_sec, year=year,
                                 landmark='🧠' in body, body=body.strip(),
                                 annot=' '.join(annot), norm=norm_title(body)))
            i = j; continue
        i += 1
    return entries


# ------------------------------------------------------- TheBrainLab parsing
def split_links(body):
    idxs = [body.find(t) for t in ('[[', '[paper]', '[code]', '[arxiv]')]
    idxs = [k for k in idxs if k >= 0]
    if not idxs:
        return body.strip(), ''
    k = min(idxs)
    return body[:k].strip(), body[k:].strip()

def clean_links(links):
    links = re.sub(r'\[\[(\w+)\]\]\((\S+?)\)', r'[[\1](\2)]', links)   # [[x]](u) -> [[x](u)]
    links = re.sub(r'\[\[?\w+\]?\]?\(\s*\)\]?', '', links)            # drop empty ()
    links = re.sub(r'(?<!\[)\[(\w+)\]\((https?://\S+?)\)', r'[[\1](\2)]', links)  # [x](u)->[[x](u)]
    return re.sub(r'\s{2,}', ' ', links).strip()

def norm_title(t):
    """Canonical title key for de-duplication across the two sources.

    Collapses the many ways the same paper is written: strips the venue tag,
    links, and short acronym parentheticals (e.g. "(PLIF)", "(SEW-ResNet)"),
    folds every "spiking neural network(s)" / "SNN(s)" mention to nothing, then
    keeps only lowercase alphanumerics. Two titles that survive to the same key
    (or where one is a long prefix of the other) are treated as the same work.
    """
    t = BOLD_RE.sub('', t)
    t = re.sub(r'\\?\[.*', '', t)          # drop the links region
    t = re.sub(r'\([^)]{1,18}\)', '', t)   # drop short acronym parentheticals
    t = t.lower()
    t = re.sub(r'spiking neural networks?', ' ', t)
    t = re.sub(r'\bsnns?\b', ' ', t)
    return re.sub(r'[^a-z0-9]+', '', t)

def same_work(a, b, minlen=34):
    """True if two dedup keys denote the same paper (equal or long prefix)."""
    if a == b:
        return True
    lo, hi = (a, b) if len(a) <= len(b) else (b, a)
    return len(lo) >= minlen and hi.startswith(lo)

def parse_brainlab(path):
    with io.open(path, encoding='utf-8') as f:
        lines = f.read().split('\n')
    out, cur_year = [], None
    for line in lines:
        m = YEARHDR.match(line)
        if m:
            cur_year = int(m.group('y')); continue
        if cur_year is None or not line.startswith('- '):
            continue
        body = line[2:].strip()
        if not body:
            continue
        text, links = split_links(body)
        yr = None
        for bm in BOLD_RE.finditer(text):
            ym = YEAR_RE.search(bm.group('v'))
            if ym: yr = int(ym.group(0))
        yr = yr or cur_year
        nt = norm_title(text)
        if len(nt) < 6:
            continue
        out.append(dict(year=yr, title=re.sub(r'\.\s*$', '', text).strip(),
                        links=clean_links(links), norm=nt))
    return out


# ------------------------------------------------------------------ helpers
def clean_body(body):
    b = body.replace(' 🧠.', '.').replace(' 🧠 ', ' ').replace('🧠', '')
    return re.sub(r'\s+\.', '.', b).strip()

def bar(count, maxc, width=30):
    if not maxc or not count: return ''
    return '█' * max(1, round(count / maxc * width))


# ------------------------------------------------------------------- render
def render(hub, extra, lang):
    en = lang == 'en'
    hub_by = defaultdict(list)
    for e in hub: hub_by[e['year']].append(e)
    extra_by = defaultdict(list)
    for e in extra: extra_by[e['year']].append(e)

    years = sorted(set(hub_by) | set(extra_by), reverse=True)
    total_hub, total_extra = len(hub), len(extra)
    total = total_hub + total_extra
    n_landmark = sum(1 for e in hub if e['landmark'])
    combined = {y: len(hub_by[y]) + len(extra_by[y]) for y in years}
    maxc = max(combined.values())

    out = []
    A = out.append              # push one line (no trailing newline)
    def BLANK(): out.append('')  # explicit blank line
    hub_md = 'README.md' if en else 'README.zh-CN.md'

    # ---- header ----
    if en:
        A('<div align="center">'); BLANK()
        A('<h1>🗓️ Awesome Spiking Neural Networks — Timeline Edition</h1>'); BLANK()
        A('<p><em>The whole SNN field in chronological order — newest first.</em><br>')
        A('<sub>the chronological companion to the thematic <a href="README.md">Hub</a></sub></p>'); BLANK()
        A('<p><a href="TIMELINE.md"><b>🌐 English</b></a> &nbsp;·&nbsp; <a href="TIMELINE.zh-CN.md">🇨🇳 中文</a> '
          '&nbsp;|&nbsp; <a href="README.md">📚 Thematic Hub (EN)</a> &nbsp;·&nbsp; <a href="README.zh-CN.md">📚 主题版 (中文)</a></p>'); BLANK()
        A(f'<p>📄 <b>{total}</b> works ({total_hub} annotated picks + {total_extra} indexed) &nbsp;·&nbsp; '
          f'🧠 <b>{n_landmark}</b> landmarks &nbsp;·&nbsp; 🗓️ <b>{years[-1]}–{years[0]}</b></p>'); BLANK()
        A('</div>'); BLANK(); A('---'); BLANK()
        A('## 📖 How to read this page'); BLANK()
        A('This is the **chronological view** of the [Awesome Spiking Neural Networks Hub](README.md). '
          'The Hub organises everything by *topic*; this page lays the field out **by year, newest first** — '
          'so you can trace how it actually unfolded, the way the '
          '[TheBrainLab timeline](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks) does.'); BLANK()
        A('Each year has **two tiers**:'); BLANK()
        A(f'- **⭐ Curated picks** — the Hub\'s **{total_hub}** deeply-annotated entries. Every line carries a '
          '*why it matters* note, a topic tag (e.g. `🎓 Training`, `⚙️ Hardware`) linking back to the full '
          'thematic section, and **🧠 = field landmark**.')
        A(f'- **➕ Full-year index** — a collapsible list of **{total_extra}** further papers, merged from '
          '[TheBrainLab](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks) and de-duplicated '
          'against the picks, so the year\'s conference output is complete (title · venue · links).'); BLANK()
        A('> **Auto-generated** — do not edit this file by hand. Add curated entries to [README.md](README.md), '
          'refresh [the index snapshot](tools/data/thebrainlab-snapshot.md), then run '
          '`python tools/build_timeline.py`. Credit for the conference index goes to '
          '[TheBrainLab/Awesome-Spiking-Neural-Networks](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks).')
    else:
        A('<div align="center">'); BLANK()
        A('<h1>🗓️ 脉冲神经网络精选 — 时间线版</h1>'); BLANK()
        A('<p><em>用时间顺序讲完整个脉冲神经网络领域 — 最新在前。</em><br>')
        A('<sub>主题版 <a href="README.zh-CN.md">Hub</a> 的时间线姊妹篇</sub></p>'); BLANK()
        A('<p><a href="TIMELINE.md">🌐 English</a> &nbsp;·&nbsp; <a href="TIMELINE.zh-CN.md"><b>🇨🇳 中文</b></a> '
          '&nbsp;|&nbsp; <a href="README.zh-CN.md">📚 主题版 (中文)</a> &nbsp;·&nbsp; <a href="README.md">📚 Thematic Hub (EN)</a></p>'); BLANK()
        A(f'<p>📄 <b>{total}</b> 篇成果（{total_hub} 篇精选注释 + {total_extra} 篇索引） &nbsp;·&nbsp; '
          f'🧠 <b>{n_landmark}</b> 项里程碑 &nbsp;·&nbsp; 🗓️ <b>{years[-1]}–{years[0]}</b></p>'); BLANK()
        A('</div>'); BLANK(); A('---'); BLANK()
        A('## 📖 如何阅读本页'); BLANK()
        A('这是 [脉冲神经网络精选 Hub](README.zh-CN.md) 的**时间线视图**。Hub 按*主题*组织；'
          '本页把整个领域按**年份倒序**铺开——让你顺着时间看清它是怎么一步步走过来的，'
          '就像 [TheBrainLab 的时间线](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks) 那样。'); BLANK()
        A('每个年份分**两层**：'); BLANK()
        A(f'- **⭐ 精选** — Hub 中 **{total_hub}** 篇带深度注释的条目。每条都有一句*为什么重要*、'
          '一个可跳回主题章节的标签（如 `🎓 训练方法`、`⚙️ 神经形态硬件`），**🧠 = 领域里程碑**。')
        A(f'- **➕ 当年全量索引** — 可折叠列表，收录另外 **{total_extra}** 篇论文，来自 '
          '[TheBrainLab](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks) 并已与精选去重，'
          '让当年的会议产出更完整（标题 · 会议 · 链接）。'); BLANK()
        A('> **自动生成** — 请勿手工编辑本文件。精选条目请加到 [README.zh-CN.md](README.zh-CN.md)，'
          '刷新[索引快照](tools/data/thebrainlab-snapshot.md)后运行 `python tools/build_timeline.py`。'
          '会议索引部分来自 [TheBrainLab/Awesome-Spiking-Neural-Networks](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks)，特此致谢。')

    # ---- activity chart ----
    BLANK(); A('---'); BLANK()
    A('## 📊 ' + ('Papers by year' if en else '逐年论文量')); BLANK()
    A('```')
    for y in [y for y in years if y >= 2010]:
        c = combined[y]
        A(f'{y}  {bar(c, maxc):<30} {c}')
    older = [y for y in years if y < 2010]
    if older:
        oc = sum(combined[y] for y in older)
        A(f'{"≤2009":<5} {bar(oc, maxc):<30} {oc}')
    A('```'); BLANK()
    A('<sub>' + ('The 2018 surrogate-gradient breakthrough and the 2023 spiking-Transformer wave stand out as the two big steps up.'
               if en else '2018 年代理梯度的突破与 2023 年脉冲 Transformer 浪潮，是图中两级明显的跃升。') + '</sub>')

    # ---- year index ----
    BLANK(); A('---'); BLANK()
    A('## 🧭 ' + ('Jump to a year' if en else '跳转到年份')); BLANK()
    A(' · '.join(f'[{y}](#-{y})' for y in years))

    # ---- eras / years ----
    for (s, e2, ten, tzh) in ERAS:
        yrs = [y for y in years if s <= y <= e2]
        if not yrs: continue
        BLANK(); A('---'); BLANK()
        span = f'{yrs[-1]}–{yrs[0]}' if len(yrs) > 1 else f'{yrs[0]}'
        A(f'## {(ten if en else tzh)}  <sub>({span})</sub>')
        for y in yrs:
            picks = sorted(hub_by[y], key=lambda x: (not x['landmark'], x['section']))
            more = extra_by[y]
            BLANK(); A(f'### 📅 {y}'); BLANK()
            if picks:
                A('**⭐ Curated picks**' if en else '**⭐ 精选**'); BLANK()
                for it in picks:
                    emoji, ltag, ztag, en_anchor, zh_anchor = SECTION_TAGS[it['section']]
                    label = ltag if en else ztag
                    anchor = en_anchor if en else zh_anchor
                    tag = f'[`{emoji} {label}`]({hub_md}{anchor})'
                    mark = ' 🧠' if it['landmark'] else ''
                    A(f'- {tag}{mark} · {clean_body(it["body"])}')
                    if it['annot']:
                        A(f'  > {it["annot"]}')
                BLANK()
            if more:
                lbl = (f'➕ {len(more)} more {y} papers' if en
                       else f'➕ 当年另有 {len(more)} 篇')
                sub = (' — conference index, via TheBrainLab' if en
                       else ' — 会议索引，来自 TheBrainLab')
                A(f'<details>')
                A(f'<summary><b>{lbl}</b>{sub}</summary>'); BLANK()
                for m in more:
                    line = f'- {m["title"]}'
                    if m['links']:
                        line += f' {m["links"]}'
                    A(line)
                BLANK(); A('</details>')

    # ---- footer ----
    BLANK(); A('---'); BLANK(); A('<div align="center">'); BLANK()
    if en:
        A('<sub>Curated picks auto-extracted from <a href="README.md">README.md</a> · '
          'conference index from <a href="https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks">TheBrainLab</a> · '
          'built by <a href="tools/build_timeline.py">tools/build_timeline.py</a>.</sub><br>')
        A('<sub>If this helps your work, please ⭐ the repo and <a href="README.md#-citation">cite it</a>.</sub>')
    else:
        A('<sub>精选条目自动提取自 <a href="README.zh-CN.md">README.zh-CN.md</a> · '
          '会议索引来自 <a href="https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks">TheBrainLab</a> · '
          '由 <a href="tools/build_timeline.py">tools/build_timeline.py</a> 生成。</sub><br>')
        A('<sub>如果本项目对你有帮助，欢迎 ⭐ 并 <a href="README.zh-CN.md#-citation">引用</a>。</sub>')
    A('</div>'); BLANK()
    return '\n'.join(out)


def main():
    brain = parse_brainlab(SNAPSHOT)
    for src, dst, lang in (('README.md', 'TIMELINE.md', 'en'),
                           ('README.zh-CN.md', 'TIMELINE.zh-CN.md', 'zh')):
        hub = parse_hub(os.path.join(ROOT, src))
        hub_norms = {e['norm'] for e in hub}
        hub_long = [n for n in hub_norms if len(n) >= 34]
        # de-dup brainlab against hub (equal or long-prefix) AND internally
        extra, seen = [], []
        for e in brain:
            k = e['norm']
            if k in hub_norms or any(same_work(k, h) for h in hub_long):
                continue
            if any(same_work(k, s) for s in seen):
                continue
            seen.append(k); extra.append(e)
        text = render(hub, extra, lang)
        with io.open(os.path.join(ROOT, dst), 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        print(f'wrote {dst}: {len(hub)} picks + {len(extra)} indexed = {len(hub)+len(extra)}')


if __name__ == '__main__':
    main()
