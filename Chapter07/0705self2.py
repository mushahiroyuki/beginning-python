#ファイル名 Chapter07/0705self2.py
class Bird:
    song = 'カー、カー！'
    def sing(self):
        print(self.song)

#実行
bird = Bird()
bird.sing() #←カー、カー！
birdsong = bird.sing
birdsong() #←カー、カー！
