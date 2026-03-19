# ========================================
# 第5章: 関数の定義・呼び出し
# ========================================

# --- 基本の関数定義 ---
def greet():
    print("こんにちは！")

greet()   # → こんにちは！
greet()   # 何度でも呼び出せる

# --- 関数の定義位置: 呼び出しより前に定義する ---
def say_hello():
    print("Hello!")

say_hello()

# --- 関数の中でも関数を呼べる ---
def morning_routine():
    greet()
    print("今日も頑張りましょう！")

morning_routine()

# --- ドキュメント文字列（docstring）---
def calculate_area(radius):
    """
    円の面積を計算する関数。

    引数:
        radius (float): 円の半径
    戻り値:
        float: 円の面積
    """
    import math
    return math.pi * radius ** 2

# help()でdocstringを表示できる
# help(calculate_area)
print(calculate_area(5))  # → 78.539...

# --- 関数の呼び出しの階層 ---
def step1():
    print("  step1 実行")

def step2():
    print("  step2 実行")
    step1()   # step2の中からstep1を呼ぶ

def main():
    print("main 開始")
    step2()
    print("main 終了")

main()
# → main 開始
# →   step2 実行
# →   step1 実行
# → main 終了
