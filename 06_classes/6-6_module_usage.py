# ========================================
# 第6章: クラスをモジュールとして使う
# ========================================

# 通常は別ファイル(例: player.py)にクラスを定義して
# from player import Player のようにインポートして使う
# ここでは同一ファイルで __name__ の動作を解説する

# --- __name__ 変数 ---
# このファイルを直接実行したとき: __name__ == "__main__"
# このファイルをimportしたとき:   __name__ == "モジュール名"

print(f"このファイルの __name__ = '{__name__}'")

class Team:
    """チームを管理するクラス"""

    def __init__(self, name):
        self.name = name
        self.members = []

    def add_player(self, player_name, number):
        self.members.append({"name": player_name, "number": number})

    def show_roster(self):
        print(f"\n=== {self.name} ロスター ===")
        for p in self.members:
            print(f"  #{p['number']} {p['name']}")

    def __len__(self):
        return len(self.members)

    def __str__(self):
        return f"Team({self.name}, {len(self)}名)"


# --- if __name__ == "__main__": ---
# このブロックは「直接実行したとき」だけ動く
# importされたときは動かない → テスト・デモに使う

if __name__ == "__main__":
    print("=== 直接実行されました ===")

    fc = Team("FC Python")
    fc.add_player("田中", 10)
    fc.add_player("鈴木", 7)
    fc.add_player("佐藤", 1)

    fc.show_roster()
    print(f"選手数: {len(fc)}名")
    print(fc)

# モジュールとして使う場合のイメージ:
# ─ team_module.py にクラスだけ書く
# ─ main.py で from team_module import Team してから使う
