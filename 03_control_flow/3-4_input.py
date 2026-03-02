# ========================================
# 第3章: input関数
# ========================================

# input()は常に「文字列(str)」を返す！

# --- 基本の使い方 ---
name = input("名前を入力してください: ")
print(f"こんにちは、{name}さん！")

# --- 数値として使う場合は型変換が必要 ---
age_str = input("年齢を入力してください: ")
age = int(age_str)    # str → int に変換
print(f"来年は{age + 1}歳です")

# 1行で書く場合
# age = int(input("年齢: "))

# --- 例 BMI計算機 ---
print("=== BMI計算機 ===")
weight = float(input("体重(kg)を入力してください: "))
height = float(input("身長(m)を入力してください: "))
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.1f}")