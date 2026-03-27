# ========================================
# 第7章: 例外処理
# ========================================

# --- 基本の try / except ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("エラー: 0で割ることはできません")

# --- 複数の例外を捕捉 ---
def safe_convert(s):
    try:
        return int(s)
    except ValueError:
        print(f"エラー: '{s}' は整数に変換できません")
        return None
    except TypeError:
        print("エラー: 型が正しくありません")
        return None

print(safe_convert("42"))    # → 42
print(safe_convert("abc"))   # → エラー: 'abc' は整数に変換できません None
print(safe_convert(None))    # → エラー: 型が正しくありません None

# --- else: 例外が発生しなかった場合 ---
try:
    val = int("100")
except ValueError:
    print("変換失敗")
else:
    print(f"変換成功: {val}")   # → 変換成功: 100

# --- finally: 必ず実行される（後片付けに使う）---
def read_data(filename):
    f = None
    try:
        f = open(filename, "r", encoding="utf-8")
        return f.read()
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {filename}")
        return ""
    finally:
        if f:
            f.close()   # エラーがあっても必ずclose
            print("ファイルをクローズしました")

# --- as で例外オブジェクトを受け取る ---
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError as e:
    print(f"IndexError 発生: {e}")

# --- 実践例: 安全なリスト要素取得 ---
def safe_get(lst, index, default=None):
    try:
        return lst[index]
    except IndexError:
        return default

data = [10, 20, 30]
print(safe_get(data, 1))     # → 20
print(safe_get(data, 99))    # → None
print(safe_get(data, 99, 0)) # → 0

# --- 例外の種類 ---
# ValueError      : 値が不正（int("abc") など）
# TypeError       : 型が不正（"a" + 1 など）
# IndexError      : インデックスが範囲外
# KeyError        : 辞書に存在しないキー
# FileNotFoundError: ファイルが存在しない
# ZeroDivisionError: 0除算