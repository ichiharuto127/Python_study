# ========================================
# 第6章: クラスメソッド・静的メソッド
# ========================================

class Player:
    team_name = "FC Python"
    _registry = []   # 全選手を管理するリスト（クラス変数）

    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.position = position
        self.goals = 0
        Player._registry.append(self)   # 生成時に登録

    def score(self, n=1):
        self.goals += n

    def __str__(self):
        return f"#{self.number} {self.name}"

    # --- インスタンスメソッド: selfを受け取る ---
    def introduce(self):
        print(f"私は{Player.team_name}の{self.name}です")

    # --- クラスメソッド: cls（クラス自身）を受け取る ---
    # インスタンスなしで呼べる。ファクトリメソッドによく使う
    @classmethod
    def get_team_name(cls):
        return cls.team_name

    @classmethod
    def get_all_players(cls):
        return cls._registry

    @classmethod
    def from_string(cls, player_str):
        """文字列から選手を生成するファクトリメソッド"""
        # "田中,10,FW" のような文字列から作る
        name, number, position = player_str.split(",")
        return cls(name, int(number), position)

    # --- 静的メソッド: self も cls も受け取らない ---
    # クラスや状態に依存しないユーティリティ関数
    @staticmethod
    def is_valid_number(number):
        return 1 <= number <= 99


# クラスメソッドはインスタンスなしで呼べる
print(Player.get_team_name())   # → FC Python

# ファクトリメソッドで生成
p1 = Player.from_string("田中,10,FW")
p2 = Player.from_string("鈴木,7,MF")
p1.score(3)
p2.score(1)

# 全選手を取得
for p in Player.get_all_players():
    print(f"{p}: {p.goals}ゴール")

# 静的メソッド
print(Player.is_valid_number(10))    # → True
print(Player.is_valid_number(100))   # → False
