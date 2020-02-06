#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0916-generator-comprehension.py
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
g = ((i + 2) ** 2 for i in range(2, 27))
print(next(g)) #← 16
print(next(g)) #← 25
print(next(g)) #← 36
print(next(g)) #← 49
print(next(g)) #← 64
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
print("-----")
#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。
print(sum(i ** 2 for i in range(10))) #← 285 = 1+4+9+16+25+36+49+64+81
#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。
