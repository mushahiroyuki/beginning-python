#ファイル名 Chapter27/config.py (listing27-2.py)
# Squishの設定ファイル
# -----------------------------

# 下の設定変数は変更可能
# ゲームの動きが速すぎたり遅すぎたりする場合は、
# スピード関連の変数を変更する

# 他の画像を使うには、以下の変数を変更
banana_image = 'banana.png'
weight_image = 'weight.png'
splash_image = 'weight.png'

# 全般的な表示を変えるには、以下の変数を変更
screen_size = 800, 600
background_color = 255, 255, 255
margin = 30
full_screen = 0 # 0: ウィンドウ   1: フルスクリーン
font_size = 36
font_name = "ヒラキノ角コシックw3ttc"
#@# font_name = "ヒラキノ角コシックw0ttc"
#@# 
# 下記を実行して表示されるフォントを指定可能
# >>> import pygame
# >>> pygame.font.get_fonts()
# 参考ページ:
#   http://to-codes.cocolog-wbs.com/blog/2017/10/pygame-ae36.html

# 以下の変数は、このゲームの動きに影響
drop_speed = 10  # 原著は1
banana_speed = 10
speed_increase = 3
weights_per_level = 10
banana_pad_top = 40
banana_pad_side = 20
