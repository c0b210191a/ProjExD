import pygame as pg
import sys
from random import randint
import random
import os
from pygame.locals import *
import time
import tkinter as tk

WIDTH = 1600
HEIGHT = 900
BLOCK_LOCAT1 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

BLOCK_LOCAT2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]



class Screen:    #??????????????????

    def __init__(self,title,wh,file):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(file)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:     #???????????????????????????
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


class Block:    #??????????????????
    def __init__(self):
        self.sfc = pg.image.load("fig/block.jpg")
        self.sfc = pg.transform.scale(self.sfc,(50,50))
        self.rct = self.sfc.get_rect()
        

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,x,y,scr:Screen):
        self.rct.center = 25+50*x, 25+50*y
        self.blit(scr)


class Bomb:     #??????????????????

    def __init__(self,color,radius,vxy,scr:Screen):
        self.sfc = pg.Surface((radius*20, radius*20)) # ??????Surface
        self.sfc.set_colorkey((0, 0, 0)) # ???????????????????????????????????????
        pg.draw.circle(self.sfc, color, (radius*10, radius*10), radius*10) # ????????????????????????
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr:Screen,bcr:Block):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        y, t = check(self.rct, bcr.rct)
        self.vx *= yoko*y
        self.vy *= tate*t
        self.blit(scr)


class Change:  #???????????????????????????

    def __init__(self):
        self.num = randint(0,9) #????????????????????????????????????
        self.size = randint(2,8)  #??????????????????????????????
        self.file_lst = ["???.jpg","??????.jpg","?????????.jpg","??????.jpg","???.jpg"]  #??????????????????????????????#?????? #17
        
    def kimg(self):
        file = f"fig/{self.num}.png"  #???????????????????????????????????????
        main(kokaton=file)

    def bomb(self):    #????????????????????????????????????
        main(size=self.size)

    def bgimg(self):    #?????????????????????????????????
        bg_file = f"fig/{random.choice(self.file_lst)}"
        main(bg=bg_file) 

    def ranbro(self):
        ls_bro = [[] for _ in range(18)]
        for i in range(18):
            for j in range(32):
                ls_bro[i].append(randint(0,1))
        main(ls = ls_bro,mana = 1)


def check_bound(obj_rct, scr_rct):     #??????
    """
    obj_rct??????????????????rct?????????????????????rct
    scr_rct??????????????????rct
    ????????????+1???????????????-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

def check(obj_rct,scr_rct):   #????????????????????????????????????
    yoko, tate = 1, 1
    if obj_rct.left+20 == scr_rct.left or scr_rct.right == obj_rct.right+1550:
        yoko = -1
    if obj_rct.top+20 == scr_rct.top or scr_rct.bottom == obj_rct.bottom+850:   #??????????????????C0B21171
        tate = -1
    return yoko,tate

main_dir = os.path.split(os.path.abspath(__file__))[0]
def load_sound(file):    #???????????????
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


def main(kokaton="fig/6.png",size=5,bg="fig/???.jpg",count = 0,ls = [],mana = 0):
    scr = Screen("???????????????????????????",(WIDTH, HEIGHT),bg)
    kkt = Bird(kokaton,2.0,(900, 400))    
    bkd = Bomb((255, 0, 0),size,(+1,+1),scr)
    chg = Change()
    bcr = Block()
    
    boom_sound = load_sound("boom.wav")   #?????????????????????
    if pg.mixer:  #BGM?????????
        music = os.path.join(main_dir, "data", "house_lo.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

    clock = pg.time.Clock()

    bad = 0
    while True:
        scr.blit()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            if event.type == pg.KEYDOWN and event.key ==pg.K_F1:  #????????????????????? ???????????????????????????
                main(count=8000)
                return
            if event.type == pg.KEYDOWN and event.key ==pg.K_F2:    #???????????????????????????????????????
                chg.kimg()
                return
            if event.type == pg.KEYDOWN and event.key ==pg.K_F3: #????????????????????????????????????
                chg.bomb()
                return
            if event.type == pg.KEYDOWN and event.key ==pg.K_F4: #?????????????????????????????????
                chg.bgimg()  
                return     
            if event.type == pg.KEYDOWN and event.key ==pg.K_F5:
                chg.ranbro()
                return

        kkt.update(scr)
        bkd.update(scr,bcr)

        count += 1


        if count >= 4000:
            bkd.update(scr,bcr)
        if count >= 8000:
            bkd.update(scr,bcr)


        if count >= 2000:
            for i,bl in enumerate(BLOCK_LOCAT1):
                for j in range(32):   #??????????????????
                    if bl[j] == 1:
                            bcr.update(j,i,scr)
                            
        if count >= 6000:
            for i,bl in enumerate(BLOCK_LOCAT2):
                for j in range(32):   #??????????????????
                    if bl[j] == 1:
                            bcr.update(j,i,scr)

        if mana == 1:
            for i,bl in enumerate(ls):
                    for j in range(32):   #??????????????????
                        if bl[j] == 1:
                                bcr.update(j,i,scr)
        
        if count >= 10000:
            root = tk.Tk()
            root.title("game")
            root.geometry("1000x400")
            root.resizable(True,True)
            if bad == 0:
                label = tk.Label(root,text="Clear",font=("",50))
            else:
                label = tk.Label(root,text=f"you lose",font=("",50))
            label.pack()
            root.mainloop()
            return

        if kkt.rct.colliderect(bkd.rct): 
            boom_sound.play()   #?????????????????????
            fonto = pg.font.Font(None,400)
            txt = fonto.render("Explosion",True,(0,0,0))
            scr.sfc.blit(txt,(100,200))
            bad += 1
            
        pg.display.update() 
        clock.tick(1000)

    

if __name__ == "__main__":
    pg.init() # ?????????
    main()    # ??????????????????
    pg.quit() # ??????????????????
    sys.exit()
