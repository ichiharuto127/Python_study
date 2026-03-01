# ========================================
# 第2章: math・randomモジュール
# ========================================

# ===== mathモジュール =====
import math

print(math.pi)           # → 3.14159...  円周率
print(math.e)            # → 2.71828...  自然対数の底
print(math.sqrt(25))     # → 5.0         平方根
print(math.log(100, 10)) # → 2.0         対数（底10）
print(math.log2(8))      # → 3.0         2を底とする対数
print(math.sin(math.pi)) # → ~0.0        サイン
print(math.cos(0))       # → 1.0         コサイン
print(math.floor(4.7))   # → 4           切り捨て
print(math.ceil(4.2))    # → 5           切り上げ

# 応用: 円の面積と円周
r = 5
area = math.pi * r ** 2
circumference = 2 * math.pi * r
print(f"半径{r}の円: 面積={area:.2f}, 円周={circumference:.2f}")

# ===== randomモジュール =====
import random

# ランダムな整数 [a, b] (両端含む)
print(random.randint(1, 6))     # サイコロ: 1〜6

# ランダムな小数 [0.0, 1.0)
print(random.random())

# ランダムな小数 [a, b]
print(random.uniform(0, 100))

# リストからランダムに1つ選ぶ
sports = ["サッカー", "バスケ", "野球", "テニス"]
print(random.choice(sports))

# リストをシャッフル（元のリストが変わる）
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # → 順番がランダムに変わる

# リストからk個をランダムに選ぶ（重複なし）
print(random.sample(range(1, 43), 6))  # ロト6風

# 再現性のある乱数（シードを固定）
random.seed(42)
print(random.randint(1, 100))  # 常に同じ値が出る

# ===== asで別名をつけてインポート =====
import math as m
print(m.sqrt(144))   # → 12.0

import random as rand
print(rand.randint(1, 10))

# ===== fromでそのまま使う =====
from math import pi, sqrt
print(pi)       # math. が不要
print(sqrt(9))  # → 3.0
