#ファイル名 Chapter27/weights.py (listing27-1.py)
import sys, pygame
from pygame.locals import *
from random import randrange

class Weight(pygame.sprite.Sprite):

    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        # image and rect used when drawing sprite:
        # スプライト描画に使う画像とレクタングル
        self.image = weight_image
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        """
        Move the weight to a random position at the top of the screen.
        画面最上部のランダムな位置にウェイトを移動する
        """
        self.rect.top = -self.rect.height
        self.rect.centerx = randrange(screen_size[0])

    def update(self):
        """
        Update the weight for display in the next frame.
        次のフレームでの表示用にウェイトを更新する
        """
        self.rect.top += self.speed
        if self.rect.top > screen_size[1]:
            self.reset()

# Initialize things
# 全体の初期化
pygame.init()
screen_size = 800, 600
pygame.display.set_mode(screen_size, FULLSCREEN)
pygame.mouse.set_visible(0)

#@# Load the weight image
# ウェイトの画像の読み込み
weight_image = pygame.image.load('weight.png')
weight_image = weight_image.convert() # ... to match the display

#@# You might want a different speed, of courase
# もちろん、スピードは自由に変えて構いません
speed = 5

#@# Create a sprite group and add a Weight
# スプライトグループを生成し、Weightをそこに付加する
sprites = pygame.sprite.RenderUpdates()
sprites.add(Weight(speed))

#@# Get the screen surface and fill it
# 画面全体を表すサーフェスを取得して塗りつぶす
screen = pygame.display.get_surface()
bg = (255, 255, 255) # 白
screen.fill(bg)
pygame.display.flip()

#@# Used to erase the sprites:
# スプライト消去用
def clear_callback(surf, rect):
    surf.fill(bg, rect)

while True:
#@# # Check for quit events:
    # 終了イベントのチェック
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
#@# # Erase previous positions:
    # 前の位置の消去
    sprites.clear(screen, clear_callback)
#@# # Update all sprites:
    # 全スプライトの更新
    sprites.update()
#@# # Draw all sprites:
    # 全スプライトの描画
    updates = sprites.draw(screen)
#@# # Update the necessary parts of the display:
    # 表示の更新（要更新部分のみ）
    pygame.display.update(updates)
