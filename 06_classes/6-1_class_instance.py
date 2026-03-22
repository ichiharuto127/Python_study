# ========================================
# 第6章: クラス・インスタンス定義
# ========================================


# --- 基本のクラス定義 ---
class Player:
    """サッカー選手を表すクラス"""

    def __init__(self, name, number, position):
        """初期化メソッド（コンストラクタ）"""
        # self.変数名 でインスタンス変数を定義
        self.name = name
        self.number = number
        self.position = position

    def introduce(self):
        """自己紹介メソッド"""
        print(f"#{self.number} {self.name} ({self.position})")

    def __str__(self):
        """print()で表示したときの文字列を定義"""
        return f"Player({self.name}, #{self.number})"


# --- インスタンスの生成 ---
p1 = Player("田中", 10, "FW")
p2 = Player("鈴木", 7, "MF")
p3 = Player("佐藤", 1, "GK")

# インスタンス変数へのアクセス
print(p1.name)      # → 田中
print(p1.number)    # → 10
print(p1.position)  # → FW

# メソッドの呼び出し
p1.introduce()      # → #10 田中 (FW)
p2.introduce()      # → #7  鈴木 (MF)

# __str__ の確認
print(p1)           # → Player(田中, #10)

# --- 各インスタンスは独立している ---
print(p1.name == p2.name)   # → False
print(p1 is p2)             # → False （別オブジェクト）

# --- インスタンスのリスト ---
team = [p1, p2, p3]
for player in team:
    player.introduce()
