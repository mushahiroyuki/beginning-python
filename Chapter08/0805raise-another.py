#ファイル名 Chapter08/0805raise-another.py
try:
    1/0
except ZeroDivisionError:
    raise ValueError