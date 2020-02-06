class Basket:  # クラスの定義の始まり

    # selfは自分を指す。いつでも使える
    def __init__(self, contents=None): # 初期化
        self.contents = contents or [] 

    def add(self, element):  # 要素を追加
        self.contents.append(element) 
            
    def print_me(self):  # 各要素を出力
        result = "" 
        for element in self.contents: 
            result = result + " " + repr(element) 
        print("現在の中身：", result) 
