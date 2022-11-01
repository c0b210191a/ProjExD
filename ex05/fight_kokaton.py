import pygame as pg
import sys
from random import randint
import random
import os


class Screen:

    def __init__(self,title,wh,file):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(file)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self,file,size,location):
        self.sfc = pg.image.load(file)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rct = self.sfc.get_rect()
        self.rct.center = location

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in self.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, self.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr)


class Bomb:

    def __init__(self,color,radius,vxy,scr:Screen):
        self.sfc = pg.Surface((radius*20, radius*20)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius*10, radius*10), radius*10) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

class Change:  #新クラス　キー入力

    def __init__(self):
        self.num = random.randint(0,9) #こうかとん画像　ランダム
        self.size = random.randint(2,8)  #爆弾サイズ　ランダム
        self.file_lst = ["bg1.jpg","bg2.jpg","bg3.jpg","bg4.jpg","bg5.jpg"]  #背景画像ランダム
        
    def kimg(self):
        file = f"fig/{self.num}.png"  #追加機能　画像ランダム選出
        main(kokaton=file)

    def bomb(self):    #追加機能　爆弾サイズ変更
        main(size=self.size)

    def bgimg(self):    #追加機能　背景画像変更
        bg_file = f"fig/{random.choice(self.file_lst)}"
        main(bg=bg_file) 


def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_sound(file):    #音声の追加
    """because pygame can be be compiled without mixer."""
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None


def main(kokaton="fig/6.png",size=1,bg="fig/pg_bg.jpg"):
    
    scr = Screen("逃げろ！こうかとん",(1600, 900),bg)
    kkt = Bird(kokaton,2.0,(900, 400))    
    bkd = Bomb((255, 0, 0),size,(+1,+1),scr)
    chg = Change()

    boom_sound = load_sound("boom.wav")   #被弾時の効果音
    if pg.mixer:  #BGMの追加
        music = os.path.join(main_dir, "data", "house_lo.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

    clock = pg.time.Clock()
    while True:
        scr.blit()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key ==pg.K_F1:  #リセットボタン ゲームを初期化する
                main()
                return

            if event.type == pg.KEYDOWN and event.key ==pg.K_F2:    #追加機能　画像ランダム選出
                chg.kimg()
                return
                

            if event.type == pg.KEYDOWN and event.key ==pg.K_F3: #追加機能　爆弾サイズ変更
                chg.bomb()
                return

            if event.type == pg.KEYDOWN and event.key ==pg.K_F4: #追加機能　背景画像変更
                chg.bgimg()  
                return     

            

        kkt.update(scr)
        bkd.update(scr)

        #score = 0   #被弾回数
        if kkt.rct.colliderect(bkd.rct): 
            boom_sound.play()   #被弾時に効果音
            #score += 1
            fonto = pg.font.Font(None,400)
            txt = fonto.render("Explosion",True,(0,0,0))
            scr.sfc.blit(txt,(100,200))
            

        pg.display.update() 
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
