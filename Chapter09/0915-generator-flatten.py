#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0915-generator-flatten.py
def flatten(nested):
     for sublist in nested:
         for element in sublist:
             yield element
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
#実行
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
nested = [[1, 2], [3, 4], [5]]
for num in flatten(nested):
    print(num)
print("-----")
print(list(flatten(nested)))
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
