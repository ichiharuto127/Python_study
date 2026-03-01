# ========================================
# 第2章: 算術演算
# ========================================

# --- 基本演算子 ---
print(10 + 3)   # →  13  加算
print(10 - 3)   # →   7  減算
print(10 * 3)   # →  30  乗算
print(10 / 3)   # →   3.333...  除算（常にfloat）
print(10 // 3)  # →   3  整数除算（切り捨て）
print(10 % 3)   # →   1  余り
print(2 ** 10)  # → 1024  累乗

# --- 演算の優先順位 ---
print(2 + 3 * 4)     # → 14  （*が先）
print((2 + 3) * 4)   # → 20  （括弧が最優先）

# --- 変数を使った計算例 ---
# BMI計算
weight = 65.0   # kg
height = 1.70   # m
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.1f}")  # → BMI: 22.5

# 速度・時間・距離
distance = 100   # km
speed = 80       # km/h
time = distance / speed
print(f"所要時間: {time:.2f}時間")  # → 所要時間: 1.25時間

# --- 切り捨て・四捨五入・切り上げ ---
import math

print(round(3.567, 1))    # → 3.6   四捨五入
print(math.floor(3.9))    # → 3     切り捨て
print(math.ceil(3.1))     # → 4     切り上げ
print(abs(-15))            # → 15    絶対値

# --- よく使う数学関数 ---
print(math.sqrt(16))       # → 4.0  平方根
print(math.pi)             # → 3.14159...
print(math.sin(math.pi/2)) # → 1.0
