# ========================================
# 第6章: クラス変数
# ========================================

# クラス変数  = クラス全体で共有される変数（全インスタンス共通）
# インスタンス変数 = 各インスタンス固有の変数

class Player:
    # --- クラス変数 ---
    team_name = "FC Python"   # チーム名（全員共通）
    player_count = 0          # 選手の人数（生成するたびに増える）

    def __init__(self, name, number, position):
        # --- インスタンス変数 ---
        self.name = name
        self.number = number
        self.position = position
        Player.player_count += 1   # クラス変数をカウントアップ

    def show_team(self):
        # クラス変数は self でも Player でもアクセスできる
        print(f"{self.name} は {Player.team_name} の選手です")

    @classmethod
    def get_count(cls):
        """クラスメソッド: インスタンスなしで呼べる"""
        return cls.player_count


# インスタンスを作るたびに player_count が増える
p1 = Player("田中", 10, "FW")
p2 = Player("鈴木", 7, "MF")
p3 = Player("佐藤", 1, "GK")

print(Player.player_count)   # → 3
print(Player.get_count())    # → 3

# クラス変数はどのインスタンスからも同じ値を参照
p1.show_team()   # → 田中 は FC Python の選手です
p2.show_team()   # → 鈴木 は FC Python の選手です

# クラス変数を変更すると全インスタンスに影響する
Player.team_name = "Python United"
p1.show_team()   # → 田中 は Python United の選手です
p2.show_team()   # → 鈴木 は Python United の選手です

# --- インスタンス変数がクラス変数を「隠す」---
p1.team_name = "個人チーム"   # p1専用のインスタンス変数が作られる
p1.show_team()   # → 田中 は 個人チーム の選手です（p1固有）
p2.show_team()   # → 鈴木 は Python United の選手です（クラス変数）
