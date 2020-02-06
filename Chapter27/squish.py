#ファイル名 Chapter27/squish.py (listing27-4.py)
import os, sys, pygame
from pygame.locals import *
import objects, config

"Squishの主要なゲーム内容の処理モジュール"

class State:

    """
    ゲームの汎用ステートクラス（ゲーム中の画面の種類を表す）。
    イベントの処理と、指定サーフェスにこのステートを表示することができる。
    """

    def handle(self, event):
        """
        終了だけを扱うデフォルトのイベント処理
        """
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()

    def first_display(self, screen):
        """
        Stateの初回の表示用。画面を背景色で塗りつぶす。
        """
        screen.fill(config.background_color)
        # 変更内容を表示に反映するため、flipを忘れずに呼び出す。
        pygame.display.flip()

    def display(self, screen):
        """
        Stateの2回目以降の表示用。デフォルトの処理内容はなし。
        """
        pass

class Level(State):
    """
    ゲームのレベル。落下させたウェイトの数のカウント、スプライトの移動、
    その他ゲームの内容に関する処理を行う。
    """

    def __init__(self, number=1):
        self.number = number
        # このレベルでかわすべき、ウェイトの残り数
        self.remaining = config.weights_per_level

        speed = config.drop_speed
        # レベル2以上ではレベルが1上がるごとにspeed_increaseを加算する
        speed += (self.number-1) * config.speed_increase
        # ウェイトとバナナを生成する
        self.weight = objects.Weight(speed)
        self.banana = objects.Banana()
        both = self.weight, self.banana # もっとスプライトを増やすこともできる……
        self.sprites = pygame.sprite.RenderUpdates(both)

    def update(self, game):
        "前のフレームからゲームステートを更新する。"
        # 全スプライトを更新する
        self.sprites.update()
        # バナナがウェイトに接触する場合、ゲームをGameOverステートに
        # 切り換えるように指示する。
        if self.banana.touches(self.weight):
            game.next_state = GameOver()
        # 接触しない場合、ウェイトが着地したらそのウェイトをリセットする。
        # このレベルのウェイトがすべてかわされたら、ゲームを
        # LevelClearedステートに切り換えるように指示する。
        elif self.weight.landed:
            self.weight.reset()
            self.remaining -= 1
            if self.remaining == 0:
                game.next_state = LevelCleared(self.number)

    def display(self, screen):
        """
        最初の表示（画面全体の消去）後にステートを表示する。firstDisplayとは異なり、
        このメソッドは、self.sprites.drawから返される、更新が必要なレクタングルの
        リストを引数としてpygame.display.updateを呼び出す。
        """
        screen.fill(config.background_color)
        updates = self.sprites.draw(screen)
        pygame.display.update(updates)

class Paused(State):
    """
    ゲームの一時停止のステート。キーボードのキーかマウスのボタンを押すと解除される。
    """

    finished = 0 # ユーザーが一時停止を解除したか？
    image = None # 画像を使う場合はそのファイル名を設定する
    text = ''    # メッセージのテキストを設定する

    def handle(self, event):
        """
        イベントを処理する。具体的にはStateに委任する場合と（通常、終了の処理を行う）、
        キーの押下とマウスクリックに対応する場合がある。後者の場合はself.finishedを
        「真」に設定する。
        """
        State.handle(self, event)
        if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
            self.finished = 1

    def update(self, game):
        """
        レベルを更新する。キーが押されるかマウスがクリックされた場合
       （self.finishedがtrue）、ゲームに対してself.next_state()（サブクラス
        で実装する）が表しているステートに切り換えるように指示する。
        """
        if self.finished:
            game.next_state = self.next_state()

    def first_display(self, screen):
        """
        初回のPausedステートの表示。画像（ある場合）を描画し、
        テキストをレンダリングする。
        """
        # まず、画面を背景色で塗りつぶして消去する
        screen.fill(config.background_color)

        # デフォルトの外観（フォントの種類）で指定サイズのFontオブジェクトを生成する
#@#      font = pygame.font.Font(None, config.font_size)
        font = pygame.font.SysFont(config.font_name, config.font_size)

        # self.textのテキストを取得し、先頭と末尾の空行を削除する
        lines = self.text.strip().splitlines()

        # テキスト一行の高さを求めるため、テキストの高さを取得する
        # （font.get_linesize()使用）
        height = len(lines) * font.get_linesize()

        # テキストの配置位置を求める（画面内でセンタリング）
        center, top = screen.get_rect().center
        top -= height // 2

        # 表示する画像がある場合
        if self.image:
            # それを読み込む
            image = pygame.image.load(self.image).convert()
            # 長方形境界を取得する
            r = image.get_rect()
            # 画像の高さの半分だけ下にテキストを移動させる
            top += r.height // 2
            # 画像をテキストより20ピクセル分上に配置する
            r.midbottom = center, top - 20
            # 画像を画面に転送する
            screen.blit(image, r)

        antialias = 1   # テキストを滑らかにする
        black = 0, 0, 0 # 表示色は黒

        # 全行をレンダリングする。計算で求めたtopの位置から始めて、
        # 各行ごとにfont.get_linesize()ピクセルずつ下に移る。
        for line in lines:
            text = font.render(line.strip(), antialias, black)
            r = text.get_rect()
            r.midtop = center, top
            screen.blit(text, r)
            top += font.get_linesize()
        # 全変更内容を表示に反映させる
        pygame.display.flip()

class Info(Paused):

    """
    ゲームについての情報を表示する一時停止のステート。
    次のステートはLevelステート（レベル1）
    """

    next_state = Level
#@#     text = '''
#@#    In this game you are a banana,
#@#    trying to survive a course in
#@#    self-defense against fruit, where the
#@#    participants will "defend" themselves
#@#    against you with a 16 ton weight.'''
    text = '''
    このゲームでは、あなたはバナナです。
    16トンの「おもり」が落ちてきますが、
    それをかわして生き延びてください。'''

class StartUp(Paused):

    """
    スプラッシュ画像と歓迎メッセージを表示する一時停止ステート。
    この後はInfoステートに移行する。
    """

    next_state = Info
    image = config.splash_image
#@#    text = '''
#@#    Welcome to Squish,
#@#    the game of Fruit Self-Defense'''

    text = '''
    果物が我が身（実）を守るゲーム
    Squishにようこそ'''

class LevelCleared(Paused):
    """
    プレイヤーが現在のレベルをクリアしたことを知らせる一時停止ステート。
    この後は次のレベルのステートに移行する。
    """

    def __init__(self, number):
        self.number = number
#@#        self.text = '''Level {} cleared
#@#        Click to start next level'''.format(self.number)
        self.text = '''レベル {} クリア
        クリックで次のレベルを開始'''.format(self.number)

    def next_state(self):
        return Level(self.number + 1)

class GameOver(Paused):

    """
    プレイヤーが失敗してゲーム終了したことを知らせるステート。
    この後はレベル1のステートに移行する。
    """

    next_state = Level
#@#    text = '''
#@#    Game Over
#@#    Click to Restart, Esc to Quit'''
    text = '''
    ゲームオーバー
    クリックで再ゲーム、［Esc］で終了'''

class Game:

    """
    ゲームステート間の移行を含め、メインの
    イベントループを処理するゲームオブジェクト
    """

    def __init__(self, *args):
        # ゲームと画像を格納しているディレクトリを取得する
        path = os.path.abspath(args[0])
        dir = os.path.split(path)[0]
        # 取得したディレクトリに移動する（後で画像ファイルを開くため）
        os.chdir(dir)
        # ステートなしで開始
        self.state = None
        # イベントループの初回でStartUpに移行する
        self.next_state = StartUp()

    def run(self):
        """
        このメソッドですべてが動き出す。
        重要な初期化処理を実行してメインイベントループに入る
        """
        pygame.init() # pygameの全モジュールを初期化するために必要

        # ゲームをウィンドウ内と全画面のどちらで表示するかを決める
        flag = 0                  # デフォルト（ウィンドウ）のモード

        if config.full_screen:
            flag = UFLLSCREEN     # 全画面モード
        screen_size = config.screen_size
        screen = pygame.display.set_mode(screen_size, flag)

        pygame.display.set_caption('Squish')
        pygame.mouse.set_visible(False)

        # メインループ
        while True:
            # (1) nextStateが変更されている場合、その新しいステートに移行して
            #     それを表示する（初回）
            if self.state != self.next_state:
                self.state = self.next_state
                self.state.first_display(screen)
            # (2) イベント処理を現在のステートに委譲する
            for event in pygame.event.get():
                self.state.handle(event)
            # (3) 現在のステートを更新する
            self.state.update(self)
            # (4) 現在のステートを表示する
            self.state.display(screen)

if __name__ == '__main__':
    game = Game(*sys.argv)
    game.run()
