#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter16/my_math.py
def square(x):
    '''
    数値を2乗して結果を返す
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x * x
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
if __name__ == '__main__':
    import doctest, my_math
    doctest.testmod(my_math)
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
