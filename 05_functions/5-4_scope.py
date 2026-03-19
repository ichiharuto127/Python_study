# ========================================
# 第5章: 変数のスコープ
# ========================================

# スコープ = 変数が「見える（使える）」範囲

# --- ローカル変数: 関数の中だけで使える ---
def my_func():
    local_var = "関数の中の変数"   # ローカル変数
    print(local_var)

my_func()
# print(local_var)   # → NameError! 関数の外からは見えない

# --- グローバル変数: どこからでも見える ---
global_var = "グローバル変数"

def show_global():
    print(global_var)   # 関数の中からも読める

show_global()           # → グローバル変数

# --- 同名の変数はスコープが異なる ---
x = 100   # グローバルのx

def change_x():
    x = 999   # これはローカルのx（別物！）
    print(f"関数の中: x = {x}")

change_x()
print(f"関数の外: x = {x}")   # → 100 （グローバルは変わらない）

# --- グローバル変数を関数内で変更するには global 宣言 ---
count = 0

def increment():
    global count   # グローバルのcountを使うことを宣言
    count += 1

increment()    # グローバルのcount = 1
increment()    # グローバルのcount = 2
increment()    # グローバルのcount = 3
print(count)   # → 3

# ※ globalはあまり使わないほうが良い（コードが追いにくくなる）
# 代わりに引数と戻り値を使うのがベターなスタイル

def increment_better(c):
    return c + 1

count2 = 0
count2 = increment_better(count2) # count2 = 1
count2 = increment_better(count2) # count2 = 2
count2 = increment_better(count2) # count2 = 3
print(count2)   # → 3

# --- ネストした関数とスコープ ---
def outer():
    msg = "外側の変数"

    def inner():
        print(msg)   # 外側の変数を読める（LEGB規則）

    inner()

outer()   # → 外側の変数

# LEGB規則: Python が変数を探す順番
# L: Local（ローカル）
# E: Enclosing（外側の関数）
# G: Global（グローバル）
# B: Built-in（組み込み）
