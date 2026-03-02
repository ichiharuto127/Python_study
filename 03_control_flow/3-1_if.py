# ========================================
# 第3章: 条件分岐
# ========================================

# --- 基本の if 文 ---
score = 75

if score >= 60:
    print("合格")

# --- if / else ---
temperature = 15

if temperature >= 25:
    print("暑い日です")
else:
    print("涼しい日です")

# --- if / elif / else ---
score = 82

if score >= 90:
    print("評価: A")
elif score >= 80:
    print("評価: B")   # 実行
elif score >= 70:
    print("評価: C")
else:
    print("評価: D")

# --- 比較演算子 ---
x = 10
print(x == 10)   # → True   等しい
print(x != 5)    # → True   等しくない
print(x > 5)     # → True   より大きい
print(x >= 10)   # → True   以上
print(x < 20)    # → True   より小さい
print(x <= 9)    # → False  以下

# --- 論理演算子 ---
age = 20
has_ticket = True

# and: 両方Trueのとき True
if age >= 18 and has_ticket:
    print("入場できます")

# or: どちらかがTrueのとき True
is_member = False
has_coupon = True
if is_member or has_coupon:
    print("割引が適用されます")

# not: 反転
is_raining = False
if not is_raining:
    print("今日は晴れです")

# --- 条件式（三項演算子）---
score = 70
result = "合格" if score >= 60 else "不合格"
print(result)   # → 合格

# --- in演算子との組み合わせ ---
sports = ["サッカー", "野球", "バスケ", "テニス"]
my_sport = "サッカー"

if my_sport in sports:
    print(f"{my_sport}はリストにあります")

# --- input関数と組み合わせた実践例 ---
name = input("名前を入力してください: ")
if name == "管理者":
    print("管理者モードで起動します")
else:
    print(f"こんにちは、{name}さん！")
