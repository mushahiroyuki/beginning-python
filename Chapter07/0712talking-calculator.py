#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter07/0712talking-calculator.py
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)
class Talker:
    def talk(self):
        print(f'こんにちは。私の値は{self.value}です。')
class TalkingCalculator(Calculator, Talker):
    pass
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
tc = TalkingCalculator()
tc.calculate('1 + 2 * 3')
tc.talk() #←こんにちは。私の値は7です。
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。
print(hasattr(tc, 'talk'))
print(hasattr(tc, 'fnord'))

#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list4)  # ←この行は無視してください。本文に引用するためのものです。
print(callable(getattr(tc, 'talk', None)))
print(callable(getattr(tc, 'fnord', None)))
#@@range_end(list4)  # ←この行は無視してください。本文に引用するためのものです。
