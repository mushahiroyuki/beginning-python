#ファイル名 Chapter16/listing16-1.py
from area import rect_area
height = 3
width = 4
correct_answer = 12
answer = rect_area(height, width)
if answer == correct_answer:
    print('テストに合格しました ')
else:
    print('テストに不合格でした ')
