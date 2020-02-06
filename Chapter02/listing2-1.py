# ファイル名 Chapter02/listing2-1.py
# 年月日を数値で指定すると値で与えられると英語の日付を出力する
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# 英語の日付の終わりに付く序数を表す接尾辞
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] +  7 * ['th'] \
        + ['st']

year    = input('年: ')
month   = input('月（1-12）: ')
day     = input('日（1-31）: ')

month_number = int(month)
day_number = int(day)

# リストの添字は0から始まるので「-1」が必要
month_name = months[month_number-1]
ordinal = day + endings[day_number-1] # 1st, 2nd, 3rd, 4th, ...

print(month_name + ' ' + ordinal + ', ' + year)
