# ファイル名 Chapter02/listing2-3.py
# 英文を「箱」に入れて画面中央に表示
sentence = input("英文を入力: ")

screen_width = 80  # 画面の幅（文字数）
text_width   = len(sentence)  # 長さ
box_width    = text_width + 6 # 箱の横幅
left_margin  = (screen_width - box_width) // 2

print()
print(' ' * left_margin + '+'   + '-' * (box_width-2)  +   '+')
print(' ' * left_margin + '|  ' + ' ' * text_width     + '  |')
print(' ' * left_margin + '|  ' +       sentence       + '  |')
print(' ' * left_margin + '|  ' + ' ' * text_width     + '  |')
print(' ' * left_margin + '+'   + '-' * (box_width-2)  +   '+')
print()
