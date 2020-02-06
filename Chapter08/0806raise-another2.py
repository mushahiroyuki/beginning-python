#ファイル名 Chapter08/0806raise-another2.py
try:
    1/0
except ZeroDivisionError:
    raise ValueError from None
