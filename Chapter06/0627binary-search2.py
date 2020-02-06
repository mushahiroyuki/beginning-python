#ファイル名 Chapter06/0627binary-search2.py
def search(sequence, number, lower=0, upper=None):
    if upper == None: upper = len(sequence) - 1
    # print(lower, upper)
    if lower == upper:
         assert number == sequence[upper]
         return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


#実行
seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(seq)

print(search(seq, 34))

print(search(seq, 100))

print(search(seq, 101))


