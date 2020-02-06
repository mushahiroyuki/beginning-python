#ファイル名 Chapter27/objects.py (listing27-3.py)
import pygame, config, os
from random import randrange

"Squishゲームに出てくるモノに関するモジュール。"

class SquishSprite(pygame.sprite.Sprite):

    """
    Squishの全スプライトの汎用スーパークラス。コンストラクタは画像の読み込み、
    スプライトの長方形（境界）と移動可能な領域の設定を行う。移動可能領域は
    画面サイズと余白部分で決まる。
    """

    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        shrink = -config.margin * 2
        self.area = screen.get_rect().inflate(shrink, shrink)

class Weight(SquishSprite):

    """
    落下するウェイト。画像はSquishSpriteのコンストラクタで設定し、
    このクラスのコンストラクタに引数として与えたスピードでウェイトが落下する。
    """

    def __init__(self, speed):
        super().__init__(config.weight_image)
        self.speed = speed
        self.reset()

    def reset(self):
        """
        ウェイトを画面最上部（ぎりぎり見えない位置）のランダムな水平位置に
        移動させる。
        """
        x = randrange(self.area.left, self.area.right)
        self.rect.midbottom = x, 0

    def update(self):
        """
        ウェイトを垂直方向に（下向きに）、スピードに対応する距離だけ移動させる。
        さらに、画面下端に達したかどうかに応じてlanded属性を設定する。
        """
        self.rect.top += self.speed
        self.landed = self.rect.top >= self.area.bottom

class Banana(SquishSprite):

    """
    絶体絶命のバナナ。画像はSquishSpriteのコンストラクタで設定され、
    位置は常に画面最下部付近で、水平方向はマウスの現在位置で決まる（一定の制限付き）
    """

    def __init__(self):
        super().__init__(config.banana_image)
        self.rect.bottom = self.area.bottom
        # 以下のパディングは画像内のバナナでない部分を表す。ウェイトが
        # この領域に入ってきても当たった（潰された）ことにはならない。
        self.pad_top = config.banana_pad_top
        self.pad_side = config.banana_pad_side

    def update(self):
        """
        バナナの中心のx座標をマウスの現在のx座標に設定してから、
        Rectのclampメソッドを使って移動許容範囲内に留まるように補正する。
        """
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect = self.rect.clamp(self.area)

    def touches(self, other):
        """
        バナナが他のスプライト（ウェイトなど）に接触したか判定する。
        Rectのcolliderectメソッドを使うのではなく、（上側と左右のパディングと
        Rectのinflateメソッドを使って）バナナの上側と左右の「空の」領域を含まな
        い長方形を新たに計算する。
        """
        # 実際のパディングの値を使って境界枠を縮小する
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        # 境界枠をバナナの下端に位置するように移動させる
        bounds.bottom = self.rect.bottom
        # 境界枠が他の物体の長方形境界と交差するかどうか調べる
        return bounds.colliderect(other.rect)
