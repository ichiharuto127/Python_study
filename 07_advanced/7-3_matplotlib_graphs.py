# ========================================
# 第7章: matplotlibでグラフ描画
# ========================================
# 実行: pip install matplotlib
# ※ 画像ファイルとして保存する（savefig）

import matplotlib
matplotlib.use("Agg")   # 画面表示なしで保存するモード
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 日本語フォント設定（環境によって変わる）
# plt.rcParams["font.family"] = "Noto Sans JP"  # Linux
# plt.rcParams["font.family"] = "Yu Gothic"     # Windows

# ===== 折れ線グラフ =====
months = list(range(1, 13))
goals  = [2, 1, 3, 4, 2, 5, 3, 6, 4, 7, 5, 8]

plt.figure(figsize=(8, 4))
plt.plot(months, goals, marker="o", color="steelblue", linewidth=2, label="Goals")
plt.title("Monthly Goals")
plt.xlabel("Month")
plt.ylabel("Goals")
plt.xticks(months)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("line_chart.png", dpi=100)
plt.close()
print("line_chart.png を保存しました")

# ===== 棒グラフ =====
players  = ["Tanaka", "Suzuki", "Sato", "Ito", "Kato"]
goals_bar = [20, 15, 12, 9, 7]

plt.figure(figsize=(7, 4))
bars = plt.bar(players, goals_bar, color=["steelblue", "salmon", "lightgreen", "gold", "plum"])
plt.title("Top Scorers")
plt.xlabel("Player")
plt.ylabel("Goals")
for bar, val in zip(bars, goals_bar):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
            str(val), ha="center", va="bottom", fontsize=10)
plt.tight_layout()
plt.savefig("bar_chart.png", dpi=100)
plt.close()
print("bar_chart.png を保存しました")

# ===== 散布図 =====
import random
random.seed(42)
speed  = [random.uniform(25, 38) for _ in range(20)]
goals2 = [int(s * 0.5 + random.uniform(-3, 3)) for s in speed]

plt.figure(figsize=(6, 5))
plt.scatter(speed, goals2, color="tomato", alpha=0.7, s=80)
plt.title("Speed vs Goals")
plt.xlabel("Speed (km/h)")
plt.ylabel("Goals")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("scatter.png", dpi=100)
plt.close()
print("scatter.png を保存しました")

# ===== 複数グラフを1枚に（subplot）=====
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# 左: 折れ線
axes[0].plot(months, goals, marker="o", color="steelblue")
axes[0].set_title("Monthly Goals")
axes[0].set_xlabel("Month")
axes[0].grid(True, alpha=0.3)

# 右: 棒グラフ
axes[1].bar(players, goals_bar, color="salmon")
axes[1].set_title("Top Scorers")
axes[1].set_xlabel("Player")

plt.tight_layout()
plt.savefig("combined.png", dpi=100)
plt.close()
print("combined.png を保存しました")
