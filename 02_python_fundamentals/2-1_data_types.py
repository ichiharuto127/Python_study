# ========================================
# 第2章: 型・type関数
# ========================================

# --- 基本のデータ型 ---
i = 42          # int   整数
f = 3.14        # float 小数
s = "Python"    # str   文字列
b = True        # bool  真偽値

# type()で型を確認
print(type(i))  # → <class 'int'>
print(type(f))  # → <class 'float'>
print(type(s))  # → <class 'str'>
print(type(b))  # → <class 'bool'>

# --- 型変換 ---
# int → float
print(float(10))     # → 10.0

# float → int (小数点以下切り捨て)
print(int(3.99))     # → 3

# int/float → str
print(str(100))      # → "100"
print(str(3.14))     # → "3.14"

# str → int / float
print(int("42"))     # → 42
print(float("3.14")) # → 3.14

# --- 数値演算の型 ---
print(type(10 + 3))    # → int
print(type(10 + 3.0))  # → float  (int + float = float)
print(type(10 / 2))    # → float  (/ は常にfloat)
print(type(10 // 2))   # → int    (// は整数除算)

# --- bool型は数値として扱える ---
print(True + 1)   # → 2  (True = 1)
print(False + 5)  # → 5  (False = 0)
