# ========================================
# 第4章: オブジェクト指向の概念
# ========================================

# Pythonではすべてがオブジェクト
# オブジェクト = データ（属性）+ 操作（メソッド）を持つ「もの」

# --- 組み込み型はすべてオブジェクト ---
text = "hello"
number = 42
items = [1, 2, 3]

# それぞれのオブジェクトが持つメソッドを確認
print(type(text))    # → <class 'str'>
print(type(number))  # → <class 'int'>
print(type(items))   # → <class 'list'>

# --- クラスとインスタンスのイメージ ---
# クラス  = 設計図（"str"クラス、"list"クラス など）
# インスタンス = 設計図から作った実体（"hello"、[1,2,3] など）

# str クラスのインスタンスを2つ作る
s1 = str("Python")   # str() コンストラクタで生成
s2 = str("Hello")    # str() コンストラクタで生成
print(s1, s2)        # → Python Hello

# list クラスのインスタンス
lst = list([10, 20, 30])
print(lst)           # → [10, 20, 30]

# --- dir() でオブジェクトのメソッド一覧を見る ---
print(dir(text))   # strが持つすべてのメソッドを表示

# --- isinstance() で型を確認 ---
print(isinstance(text, str))    # → True
print(isinstance(number, int))  # → True
print(isinstance(items, list))  # → True
print(isinstance(text, int))    # → False

# --- idとis：同じオブジェクトかどうか ---
a = [1, 2, 3]
b = a            # 同じオブジェクトを参照
c = [1, 2, 3]    # 別のオブジェクト（内容は同じ）

print(a is b)    # → True  （同じオブジェクト）
print(a is c)    # → False （別のオブジェクト）
print(a == c)    # → True  （値は等しい）
