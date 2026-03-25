# 第5章 学習メモ

# 問題1
• 関数を呼び出すときに関数に渡す値のことを[（1）]といい、関数から戻される値のことを[（2）]という。
• 関数に複数の値を渡すために、[（1）]をカンマ区切りで並べたものを[（3）]と呼ぶ。
• [（1）]のうち、変数の名前を指定したものを[（4）] 、値が渡されなかった場合に設定されるデフォルト値が決まっているものを[（5）]、個数が決まっていないものを[（6）]という。

# 解答
(1) 引数
(2) 戻り値(返値)
(3) 引数列
(4) キーワード引数
(5) デフォルト引数
(6) 可変長引数

# 問題2
次のようなfunc関数が定義されている。
def func(a, b = 5):
    print(a, b)
次のうち、func関数を正しく呼び出せるものを選べ。
（1） func()
（2） func(5)
（3） func(5, 10)
（4） func(a = 5)
（5） func(b = 10)
（6） func(5, b = 10)
（7） func(b = 10, a = 5)

# 解答
(2) func(5)
*a=5(必須), b=5(デフォルト)*
(3) func(5, 10)
*a=5(必須), b=10(位置)*
(4) func(a = 5)
*a=5(キーワード), b=5(デフォルト)*
(6) func(5, b = 10)
*a=5(必須), b=10(キーワード)*
(7) func(b = 10, a = 5)
*a=5(キーワード), b=10(キーワード)*

# 問題3-1
関数名: print_hello
引数名: count
処理の内容: 引数で渡されたcountの回数だけ、Helloという文字列を出力する。

# 解答
def print_hello(count):
    for i in range(0, count):
        print('Hello')
print_hello(3)

# 問題3-2
関数名: get_rectangle_area
引数名: width, height
処理の内容: 引数で渡された幅(width)と高さ(height)の値を持つ長方形の面積を返す。

# 解答
def get_rectangle_area(width, height):
    return width * height
get_rectangle_area(10, 5)

# 問題3-3
関数名: get_message
引数名: name
処理の内容: 'こんにちは{name}さん'という文字列を返す。引数が指定されなかった場合は、'名無し'という文字列をnameのデフォルト値とする。

# 解答
def get_message(name = '名無し'):
    return f'こんにちは{name}さん'
print(get_message())
print(get_message('Haruto'))

# 問題3-4
関数名: get_absolute_value
引数名: value
処理の内容: 引数で渡されたvalueの値の絶対値を返す。

# 解答
def get_absolute_value(value):
    if value < 0:
        return -value
    else:
        return value
get_absolute_value(5.5)
get_absolute_value(-3.3)

# 問題3-5
関数名: get_tail
引数名: *args
処理の内容: 可変長引数で渡された複数の引数の中で、末尾の引数の値を返す。

# 解答
def get_tail(*args):
    return args[-1]
get_tail(1, 2, 3)
get_tail(2, 3, 5, 7, 11)