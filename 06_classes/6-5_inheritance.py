# ========================================
# 第6章: 継承
# ========================================

# 継承: 既存クラス（親）の機能を引き継いで新しいクラス（子）を作る

# --- 親クラス ---
class Player:
    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.position = position

    def introduce(self):
        print(f"#{self.number} {self.name} ({self.position})")

    def __str__(self):
        return f"{self.name}(#{self.number})"


# --- 子クラス: Playerを継承 ---
class Goalkeeper(Player):
    """ゴールキーパー専用クラス"""

    def __init__(self, name, number):
        # 親クラスの__init__を呼ぶ（super()を使う）
        super().__init__(name, number, "GK")
        self.saves = 0   # GK固有の変数

    def make_save(self):
        self.saves += 1
        print(f"{self.name}がセーブ！（通算{self.saves}セーブ）")

    # メソッドのオーバーライド（上書き）
    def introduce(self):
        super().introduce()   # 親のintroduceを呼んで
        print(f"  → セーブ数: {self.saves}")


class Striker(Player):
    """ストライカー専用クラス"""

    def __init__(self, name, number):
        super().__init__(name, number, "FW")
        self.goals = 0

    def score(self):
        self.goals += 1
        print(f"{self.name}がゴール！（通算{self.goals}ゴール）")

    def introduce(self):
        super().introduce()
        print(f"  → ゴール数: {self.goals}")


# --- 使ってみる ---
gk = Goalkeeper("佐藤", 1)
st = Striker("田中", 10)

gk.make_save()      # → 佐藤がセーブ！（通算1セーブ）
gk.make_save()      # → 佐藤がセーブ！（通算2セーブ）
gk.make_save()      # → 佐藤がセーブ！（通算3セーブ）
st.score()          # → 田中がゴール！（通算1ゴール）
st.score()          # → 田中がゴール！（通算2ゴール）

print(f"{'='*5} チーム紹介 {'='*5}")
gk.introduce()      # → #1 佐藤 (GK)   → セーブ数: 3
st.introduce()      # → #10 田中 (FW)  → ゴール数: 2

# --- isinstance: 継承関係を確認 ---
print(isinstance(gk, Goalkeeper))  # → True
print(isinstance(gk, Player))      # → True  （継承しているのでPlayerでもある）
print(isinstance(st, Goalkeeper))  # → False

# --- 共通インターフェースで扱える（ポリモーフィズム）---
team = [gk, st, Player("鈴木", 7, "MF")]
for p in team:
    p.introduce()   # 各クラスの introduce() が呼ばれる
