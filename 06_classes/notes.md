# 第6章 学習メモ

# 問題1
・Pythonは[（1）]指向型の⾔語といわれ、クラスは[（1）]の属性や機能を定義したものである。
・クラスの定義の中で[（1）]の持つ情報は[（2）]に持たせることができ、機能は[（3）]に持たせることができる。
・インスタンスが⽣成されるときに⾃動的に呼び出されるメソッドを [（4）]またはコンストラクタと呼ぶ。

# 解答
(1) オブジェクト
(2) インスタンス変数
(3) メソッド
(4) 初期化メソッド (def __init__(self):)

# 問題2
空欄(A)に、問いの条件に合う関数を追加せよ。空欄(B)には、その関数を呼び出す命令⽂を記述せよ。なお、関数に戻り値がある場合は、受け取った戻り値を出⼒すること。

# 問題2-1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
[ (A) ]
a = Person("山田太郎", 20)
[ (B) ]

関数名: print_info
引数名: p (Personオブジェクト)
処理の内容: 引数で受け取るPersonオブジェクトの、名前と年齢の情報を出力する。

# 解答
(A)
def print_info(p):
    print('名前', p.name)
    print('年齢', p.age)
(B)
print_info(a)

# 問題2-2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
[ (A) ]
a = Person("山田太郎", 20)
[ (B) ]

関数名: age_check
引数名: p (Personオブジェクト), i (整数値)
処理の内容: 引数で受け取るPersonオブジェクトの年齢が、引数iの値を超えているならばTrueを、そうでない場合はFalseを返す。

# 解答
(A)
def age_check(p, i):
    return p.age > i:

(B)
age_check(a, 18)

# 問題2-3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
[ (A) ]
a = Person("山田太郎", 20)
b = Person("鈴木花子", 19)
[ (B) ]

関数名: print_younger_person_name
引数名: p1 (Personオブジェクト), p2 (Personオブジェクト)
処理の内容: 引数で受け取る2つのPersonオブジェクトのうち、年齢が若い方の名前を出力する。ただし、同じ年齢の名前の場合は'Same'を出力する。

# 解答
(A)
def print_younger_person_name(p1, p2):
    if p1.age > p2.age:
        n = p2.name
    elif p1.age < p2.age:
        n = p1.name
    else:
        n = 'Same'
    return n

(B)
print_younger_person_name(a, b)

# 問題3
class X:
    def __init__(self):
        print('[x]')
    def a(self):
        print('[x.a]')
    def b(self):
        print('[x.b]')

class Y(X):
    def __init__(self):
        super().__init__()
        print('[y]')
    def a(self):
        print ('[y.a]')
        super().a()

このプログラムに対して以下の処理でそれぞれどのような出⼒が得られるか答えよ。

x = X()     *(1)*
x.a()       *(2)*
x.b()       *(3)*
y = Y()     *(4)*
y.a()       *(5)*
y.b()       *(6)*

# 解答
(1) [x]
(2) [x.a]
(3) [x.b]
(4) [x]
    [y]
(5) [y.a]
    [x.a]
(6) [x.b]
