#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0921-queen2.py
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

def queens(num, state):
    if len(state) == num-1:
        for pos in range(num):
            if not conflict(state, pos):
                 yield pos
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
    else:
        for pos in range(num):
            if not conflict(state, pos):
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。
def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
           if len(state) == num-1:
              yield (pos,)
           else:
              for result in queens(num, state + (pos,)):
                  yield (pos,) + result
#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list5)  # ←この行は無視してください。本文に引用するためのものです。
def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
    for pos in solution:
        print(line(pos))
#@@range_end(list5)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list4)  # ←この行は無視してください。本文に引用するためのものです。
print(list(queens(3))) #← []
print(list(queens(4))) #← [(1, 3, 0, 2), (2, 0, 3, 1)]
print('-----1')
count = 0
for solution in queens(8):
    count += 1
    print(solution) #← 解を出力

print(f'解の総数: {len(list(queens(8)))}個') #← 解の総数: 92個
#@@range_end(list4)  # ←この行は無視してください。本文に引用するためのものです。
print('-----2')
#@@range_begin(list6)  # ←この行は無視してください。本文に引用するためのものです。
import random
prettyprint(random.choice(list(queens(8))))
#@@range_end(list6)  # ←この行は無視してください。本文に引用するためのものです。
