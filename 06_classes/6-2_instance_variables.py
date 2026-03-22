# ========================================
# 第6章: インスタンス変数
# ========================================

class Player:
    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.position = position
        self.goals = 0       # 初期値0で用意
        self.assists = 0

    def goal(self):
        """ゴールを記録する"""
        self.goals += 1
        print(f"{self.name}がゴール！（通算{self.goals}ゴール）")

    def assist(self):
        """アシストを記録する"""
        self.assists += 1
        print(f"{self.name}がアシスト！（通算{self.assists}アシスト）")

    def stats(self):
        """成績を表示する"""
        total = self.goals + self.assists
        print(f"{self.name}: {self.goals}G {self.assists}A ({total}pts)")


# インスタンスを作る
Tanaka = Player("田中", 10, "FW")
Suzuki = Player("鈴木", 7, "MF")

# メソッドでインスタンス変数を変更
Tanaka.goal()
Tanaka.goal()
Tanaka.assist()
Suzuki.assist()
Suzuki.assist()
Suzuki.goal()

# 各インスタンスは独自の状態を持つ
Tanaka.stats()   # → 田中: 2G 1A (3pts)
Suzuki.stats()   # → 鈴木: 1G 2A (3pts)

# --- 外からインスタンス変数を直接変更もできる ---
Tanaka.goals = 20   # 直接変更
Tanaka.stats()      # → 田中: 20G 1A (21pts)

# --- hasattr: インスタンス変数の存在確認 ---
print(hasattr(Tanaka, "goals"))    # → True
print(hasattr(Tanaka, "height"))   # → False

# --- getattr / setattr: 文字列でアクセス ---
attr_name = "name"
print(getattr(Tanaka, attr_name))        # → 田中
setattr(Tanaka, "number", 99)
print(Tanaka.number)                     # → 99
