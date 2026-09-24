"""달칩샌드 Meta 광고 원본 엑셀 → 포트폴리오 근거 이미지 생성.

원본: Meta 광고관리자 내보내기(Raw Data Report)
  - 달칩-메타-광고-데이터_성별-연령버전.xlsx  (일 · 성별 · 연령 · 광고별)
  - 2주차-영상-참여-지표.xlsx                 (2주차 지면 · 플랫폼별)
잘못 올린 광고 't1_mom_character - v3'는 모든 집계에서 제외한다.
"""
import os
from math import erfc, sqrt
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

# 원본 엑셀은 저장소에 포함하지 않는다. 기본값은 로컬 작업 폴더, 다른 위치면 DALCHIP_DATA_DIR로 지정
ROOT = Path(os.environ.get("DALCHIP_DATA_DIR", Path(__file__).resolve().parents[3]))
OUT = Path(__file__).resolve().parents[1] / "images" / "evidence"
OUT.mkdir(parents=True, exist_ok=True)
EXCLUDE = "t1_mom_character - v3"

plt.rcParams.update({"font.family": "Malgun Gothic", "axes.unicode_minus": False})
INK, INK2, MUTED, LINE = "#111111", "#444444", "#8a8a8a", "#e5e5e5"
ACCENT, ACCENT_D, ACCENT_LL, BAD, GREY = "#ff6900", "#c24e00", "#fff5ec", "#5c5c5c", "#d4d4d4"

NUM = ["지출 금액 (KRW)", "링크 클릭", "노출", "클릭(전체)", "ThruPlay"]
raw = pd.read_excel(ROOT / "달칩-메타-광고-데이터_성별-연령버전.xlsx")
n_rows, n_cols = raw.shape
d = raw[raw["광고 이름"] != EXCLUDE].copy()
for c in NUM:
    d[c] = pd.to_numeric(d[c], errors="coerce").fillna(0)
d["일"] = pd.to_datetime(d["일"])
t1 = d[d["광고 세트 이름"].str.startswith("t1")]

place = pd.read_excel(ROOT / "2주차-영상-참여-지표.xlsx")
place = place[(place["광고 이름"] != EXCLUDE) & place["광고 세트 이름"].str.startswith("t1")].copy()
place["아웃바운드 클릭"] = pd.to_numeric(place["아웃바운드 클릭"], errors="coerce").fillna(0)


def z_test(c1, n1, c2, n2):
    p = (c1 + c2) / (n1 + n2)
    z = (c1 / n1 - c2 / n2) / sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    return z, erfc(abs(z) / sqrt(2))


def header(fig, title, sub):
    fig.text(0.035, 0.955, title, fontsize=17, fontweight="bold", color=INK, va="top")
    fig.text(0.035, 0.895, sub, fontsize=10.5, color=MUTED, va="top")


def footer(fig, text):
    fig.text(0.035, 0.03, text, fontsize=9, color=MUTED)


def draw_table(ax, cols, rows, widths, hl_rows=(), align=None):
    ax.axis("off")
    n = len(rows) + 1
    h = 1 / n
    x = 0
    xs = []
    for w in widths:
        xs.append(x)
        x += w
    ax.add_patch(plt.Rectangle((0, 1 - h), 1, h, color=ACCENT_LL, transform=ax.transAxes, lw=0))
    for j, c in enumerate(cols):
        ax.text(xs[j] + 0.01, 1 - h / 2, c, fontsize=10, fontweight="bold", color=INK2, va="center", transform=ax.transAxes)
    for i, r in enumerate(rows):
        y = 1 - h * (i + 1.5)
        if i in hl_rows:
            ax.add_patch(plt.Rectangle((0, 1 - h * (i + 2)), 1, h, color="#ffebdd", transform=ax.transAxes, lw=0))
        ax.plot([0, 1], [1 - h * (i + 2)] * 2, color=LINE, lw=0.8, transform=ax.transAxes)
        for j, v in enumerate(r):
            right = align and align[j] == "r"
            ax.text(xs[j] + (widths[j] - 0.01 if right else 0.01), y, v, fontsize=10.5, color=INK,
                    va="center", ha="right" if right else "left", transform=ax.transAxes,
                    fontweight="bold" if (i in hl_rows and j == 0) else "normal")


def fmt_won(v):
    return f"₩{v:,.0f}"


# ---------- E3. 원본 데이터 발췌 ----------
cols = ["광고 세트 이름", "광고 이름", "일", "성", "연령", "지출 금액 (KRW)", "노출", "링크 클릭", "CTR(링크 클릭률)"]
sample = raw[(raw["광고 이름"] != EXCLUDE) & raw["링크 클릭"].notna()].copy()
sample["일"] = pd.to_datetime(sample["일"])
sample = sample[sample["광고 세트 이름"].str.startswith("t1")].sort_values(["일", "광고 이름", "성", "연령"]).head(12)
rows = []
for _, r in sample.iterrows():
    rows.append([r["광고 세트 이름"], r["광고 이름"], r["일"].strftime("%Y-%m-%d"), r["성"], r["연령"],
                 f"{r['지출 금액 (KRW)']:,.0f}", f"{r['노출']:,.0f}", f"{r['링크 클릭']:,.0f}", f"{float(r['CTR(링크 클릭률)']):.2f}"])
fig = plt.figure(figsize=(12, 6.4), dpi=150, facecolor="white")
header(fig, "원본 데이터 · Meta 광고관리자 내보내기", f"달칩-메타-광고-데이터_성별-연령버전.xlsx · Raw Data Report · {n_rows}행 × {n_cols}열 · 2026.07.18 – 07.31 · 일·성별·연령·광고별 (아래는 아이엄마 세트 첫 12행)")
ax = fig.add_axes([0.035, 0.1, 0.93, 0.74])
draw_table(ax, cols, rows, [0.11, 0.17, 0.11, 0.08, 0.08, 0.13, 0.1, 0.1, 0.12], align="lllllrrrr")
footer(fig, "필드명은 원본 그대로 · 이 파일을 Python(pandas)으로 소재·주차·성별·연령별로 다시 집계해 포트폴리오 수치를 검증했습니다")
fig.savefig(OUT / "ev_raw_sample.png", facecolor="white")
plt.close(fig)

# ---------- E4. 소재별·주차별 집계 + 검정 ----------
g = t1.groupby(["광고 세트 이름", "광고 이름"]).agg(
    start=("일", "min"), end=("일", "max"), spend=("지출 금액 (KRW)", "sum"), imp=("노출", "sum"),
    link=("링크 클릭", "sum"), thru=("ThruPlay", "sum")).reset_index()
order = [("t1_mom", "t1_mom_character"), ("t1_mom", "t1_mom_comedy"), ("t1_mom_v2", "t1_mom_character"), ("t1_mom_v2", "t1_mom_character_v2")]
label = {("t1_mom", "t1_mom_character"): "1주차 · 캐릭터편", ("t1_mom", "t1_mom_comedy"): "1주차 · 코미디편",
         ("t1_mom_v2", "t1_mom_character"): "2주차 · 캐릭터편", ("t1_mom_v2", "t1_mom_character_v2"): "2주차 · 캐릭터 2차(보완판)"}
rows = []
for k in order:
    r = g[(g["광고 세트 이름"] == k[0]) & (g["광고 이름"] == k[1])].iloc[0]
    rows.append([label[k], f"{r.start:%m/%d}–{r.end:%m/%d}", fmt_won(r.spend), f"{r.imp:,.0f}", f"{r.link:,.0f}",
                 f"{r.link / r.imp * 100:.2f}%", fmt_won(r.spend / r.link), f"{r.thru / r.imp * 100:.2f}%"])
tot = g[g.apply(lambda r: (r["광고 세트 이름"], r["광고 이름"]) in order, axis=1)].sum(numeric_only=True)
rows.append(["합계 (아이엄마 세트)", "07/18–07/31", fmt_won(tot.spend), f"{tot.imp:,.0f}", f"{tot.link:,.0f}",
             f"{tot.link / tot.imp * 100:.2f}%", fmt_won(tot.spend / tot.link), "—"])
z1, p1 = z_test(588, 12520, 77, 2570)
z2, p2 = z_test(1601, 47434, 73, 4332)
fig = plt.figure(figsize=(12, 6.2), dpi=150, facecolor="white")
header(fig, "소재별 성과 · 원본 엑셀 재집계", "아이엄마 타깃 세트 · 링크 클릭 기준 · 1주차 세트 t1_mom / 2주차 세트 t1_mom_v2 · 예산은 광고 세트 단위")
ax = fig.add_axes([0.035, 0.3, 0.93, 0.56])
draw_table(ax, ["소재", "기간", "지출", "노출", "링크 클릭", "링크 CTR", "링크 CPC", "끝까지 본 비율"], rows,
           [0.22, 0.12, 0.12, 0.1, 0.1, 0.11, 0.11, 0.12], hl_rows=(0, 2), align="llrrrrrr")
fig.text(0.035, 0.2, "비율 검정 (두 비율 z검정, 링크 CTR)", fontsize=11.5, fontweight="bold", color=INK)
fig.text(0.035, 0.145, f"1주차  캐릭터 4.70% vs 코미디 3.00%   →   z = {z1:.2f},  p = {p1:.1e}  (p < 0.001)", fontsize=10.5, color=INK2)
fig.text(0.035, 0.095, f"2주차  원본 3.38% vs 보완판 1.69%   →   z = {z2:.2f},  p = {p2:.1e}  (p < 0.001)", fontsize=10.5, color=INK2)
footer(fig, "끝까지 본 비율 = ThruPlay ÷ 노출 · 메타가 소재별 노출을 자동 배분한 비교라 무작위 A/B 테스트는 아님 · 잘못 올린 광고 1건(t1_mom_character - v3) 제외")
fig.savefig(OUT / "ev_creative_table.png", facecolor="white")
plt.close(fig)

# ---------- E5. 성별·연령 ----------
age = t1[t1["연령"] != "Unknown"].groupby("연령").agg(link=("링크 클릭", "sum"), imp=("노출", "sum"))
age["ctr"] = age.link / age.imp * 100
gender = t1.groupby("성")["링크 클릭"].sum()
fem = gender.get("female", 0) / gender.sum() * 100
fig = plt.figure(figsize=(12, 5.6), dpi=150, facecolor="white")
header(fig, "성별 · 연령별 반응 · 원본 엑셀 재집계", "아이엄마 타깃 세트 · 2주 합산 · 링크 클릭 기준")
ax = fig.add_axes([0.07, 0.12, 0.52, 0.62])
colors = [ACCENT if a in ("55-64", "65+") else GREY for a in age.index]
bars = ax.bar(age.index, age.ctr, color=colors, width=0.62)
for b, v in zip(bars, age.ctr):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.08, f"{v:.2f}%", ha="center", fontsize=11, fontweight="bold", color=INK)
ax.set_ylabel("링크 CTR (%)", color=INK2)
ax.set_ylim(0, age.ctr.max() * 1.25)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.spines["left"].set_color(LINE)
ax.spines["bottom"].set_color(LINE)
ax.tick_params(colors=INK2)
ax.set_title("연령별 링크 CTR", loc="left", fontsize=12, color=INK, pad=10)
old = t1[t1["연령"].isin(["55-64", "65+"])]
young = t1[t1["연령"].isin(["25-34", "35-44", "45-54"])]
old_ctr = old["링크 클릭"].sum() / old["노출"].sum() * 100
young_ctr = young["링크 클릭"].sum() / young["노출"].sum() * 100
old_share = old["링크 클릭"].sum() / t1["링크 클릭"].sum() * 100
fig.text(0.65, 0.74, "여성 비중", fontsize=12, color=INK2)
fig.text(0.65, 0.62, f"{fem:.0f}%", fontsize=34, fontweight="bold", color=ACCENT_D)
fig.text(0.65, 0.57, f"링크 클릭 {gender.sum():,.0f}건 중 {gender.get('female', 0):,.0f}건", fontsize=10.5, color=MUTED)
fig.text(0.65, 0.44, "55세 이상 vs 25~54세 링크 CTR", fontsize=12, color=INK2)
fig.text(0.65, 0.32, f"{old_ctr:.2f}% vs {young_ctr:.2f}%", fontsize=26, fontweight="bold", color=ACCENT_D)
fig.text(0.65, 0.27, f"55세 이상이 링크 클릭의 {old_share:.0f}%", fontsize=10.5, color=MUTED)
footer(fig, "출처: 달칩-메타-광고-데이터_성별-연령버전.xlsx · 성별 unknown 포함 · 연령 Unknown 1행 제외")
fig.savefig(OUT / "ev_age_gender.png", facecolor="white")
plt.close(fig)

# ---------- E6. 지면별 링크 클릭 (2주차) ----------
pl = place.groupby(["플랫폼", "노출 위치"])["아웃바운드 클릭"].sum()
pl = pl[pl > 0].sort_values()
names = {"Facebook 릴스": "페이스북 릴스", "Instagram 릴스": "인스타그램 릴스", "Threads 피드": "스레드 피드",
         "Instagram 스토리": "인스타그램 스토리", "인스트림 릴스": "페이스북 인스트림 릴스", "Facebook 알림": "페이스북 알림"}
labels = [names.get(p, ("페이스북 " if f == "facebook" else "인스타그램 " if f == "instagram" else "") + p) for f, p in pl.index]
reels = pl[[i for i in pl.index if "릴스" in i[1]]].sum()
fig = plt.figure(figsize=(12, 5.6), dpi=150, facecolor="white")
header(fig, "지면별 링크 클릭 · 원본 엑셀 재집계", f"아이엄마 타깃 세트 · 2주차(7/25–7/31) · 링크 클릭 {pl.sum():,.0f}건 · 자동 배치")
ax = fig.add_axes([0.2, 0.14, 0.5, 0.68])
cols_ = [ACCENT if "릴스" in p else GREY for _, p in pl.index]
bars = ax.barh(labels, pl.values, color=cols_, height=0.62)
for b, v in zip(bars, pl.values):
    ax.text(v + 12, b.get_y() + b.get_height() / 2, f"{v:,.0f}", va="center", fontsize=10.5, fontweight="bold", color=INK)
for s in ("top", "right", "bottom"):
    ax.spines[s].set_visible(False)
ax.spines["left"].set_color(LINE)
ax.set_xticks([])
ax.tick_params(colors=INK2, labelsize=10.5)
fig.text(0.76, 0.66, "릴스 비중", fontsize=12, color=INK2)
fig.text(0.76, 0.54, f"{reels / pl.sum() * 100:.0f}%", fontsize=34, fontweight="bold", color=ACCENT_D)
fig.text(0.76, 0.49, f"{pl.sum():,.0f}건 중 {reels:,.0f}건", fontsize=10.5, color=MUTED)
footer(fig, "출처: 2주차-영상-참여-지표.xlsx (아웃바운드 클릭 = 아마존 상품 페이지로 이동한 클릭) · 지면별 지출이 없어 비용 효율은 비교하지 않음")
fig.savefig(OUT / "ev_placement.png", facecolor="white")
plt.close(fig)

# ---------- E7. 원본 vs 보완판 (2주차) ----------
wk2 = pd.read_excel(ROOT / "2주차-영상-참여-지표.xlsx")
wk2 = wk2[wk2["광고 이름"].isin(["t1_mom_character", "t1_mom_character_v2"])].copy()
for c in ["동영상 재생", "동영상 3초 이상 재생", "동영상 25% 재생", "ThruPlay"]:
    wk2[c] = pd.to_numeric(wk2[c], errors="coerce").fillna(0)
w = wk2.groupby("광고 이름")[["동영상 재생", "동영상 3초 이상 재생", "동영상 25% 재생", "ThruPlay"]].sum()
ctr2 = t1[t1["광고 세트 이름"] == "t1_mom_v2"].groupby("광고 이름").apply(lambda x: x["링크 클릭"].sum() / x["노출"].sum() * 100)
metrics = [("3초 이상 본 비율", "동영상 3초 이상 재생"), ("25% 지점까지 본 비율", "동영상 25% 재생"), ("끝까지 본 비율", "ThruPlay")]
fig = plt.figure(figsize=(12, 5.6), dpi=150, facecolor="white")
header(fig, "원본 vs 캐릭터 2차(보완판) · 원본 엑셀 재집계", "아이엄마 타깃 세트 · 2주차(7/25–7/31) · 시청 지표는 재생 대비, 링크 CTR은 노출 대비")
ax = fig.add_axes([0.06, 0.14, 0.58, 0.64])
xs = range(len(metrics))
orig = [w.loc["t1_mom_character", c] / w.loc["t1_mom_character", "동영상 재생"] * 100 for _, c in metrics]
v2 = [w.loc["t1_mom_character_v2", c] / w.loc["t1_mom_character_v2", "동영상 재생"] * 100 for _, c in metrics]
b1 = ax.bar([x - 0.19 for x in xs], orig, width=0.36, color=ACCENT, label="원본 (채택)")
b2 = ax.bar([x + 0.19 for x in xs], v2, width=0.36, color=GREY, label="보완판")
for bars in (b1, b2):
    for b in bars:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.6, f"{b.get_height():.1f}%", ha="center", fontsize=10.5, fontweight="bold", color=INK)
ax.set_xticks(list(xs), [m for m, _ in metrics])
ax.set_ylim(0, max(orig + v2) * 1.25)
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
ax.spines["left"].set_color(LINE)
ax.spines["bottom"].set_color(LINE)
ax.tick_params(colors=INK2)
ax.legend(frameon=False, loc="upper left")
ax.set_title("시청 지표 · 보완판이 이탈을 줄임", loc="left", fontsize=12, color=INK, pad=10)
fig.text(0.7, 0.72, "목표 지표 · 링크 CTR", fontsize=12, color=INK2)
fig.text(0.7, 0.6, f"{ctr2['t1_mom_character']:.2f}%", fontsize=30, fontweight="bold", color=ACCENT_D)
fig.text(0.86, 0.615, "원본", fontsize=11, color=MUTED)
fig.text(0.7, 0.48, f"{ctr2['t1_mom_character_v2']:.2f}%", fontsize=30, fontweight="bold", color=BAD)
fig.text(0.86, 0.495, "보완판", fontsize=11, color=MUTED)
fig.text(0.7, 0.36, "시청은 늘었지만 클릭은 절반", fontsize=12, fontweight="bold", color=INK)
fig.text(0.7, 0.31, "→ 보완판을 멈추고 원본에 예산 유지", fontsize=11, color=INK2)
footer(fig, "출처: 2주차-영상-참여-지표.xlsx(시청 지표) · 달칩-메타-광고-데이터_성별-연령버전.xlsx(링크 CTR) · CPC 원본 ₩138 vs 보완판 ₩239")
fig.savefig(OUT / "ev_v2_compare.png", facecolor="white")
plt.close(fig)

print("saved to", OUT)
