import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm
import datetime

def tkobj(t1,t2):
    root = tk.Tk()
    root.title("pygame")
    root.geometry("300x100")

    time = (t2-t1).seconds  #時間保持
    label = tk.Label(root,text=f"{time}秒")  #時間を表示する
    label.pack()

    root.mainloop()

def check_bound(obj_rct,scr_rct):  #7  画面の外に出ないようにする関数
    """
    obj_rct こうかとん　または　爆弾の　rect
    scr_rct スクリーンのrect
    """
    yoko, tate = 1, 1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko,tate

def main(pic="fig/6.png",num = 1):
    st = datetime.datetime.now()
    pg.display.set_caption("逃げろ！こうかとん")   #1
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()

    bg_sfc = pg.image.load("fig/pg_bg.jpg")  
    bg_rct = bg_sfc.get_rect()

    #3
    tori_sfc = pg.image.load(pic)
    tori_sfc = pg.transform.rotozoom(tori_sfc,0 , 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    #5
    draw_sfc = pg.Surface((20*num,20*num))
    draw_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(draw_sfc, (255, 0, 0), (10*num,10*num), 10*num)  #追加機能　爆弾サイズ
    draw_rct = draw_sfc.get_rect()
    drawx = scrn_rct.width
    drawy = scrn_rct.height
    draw_rct.centerx, draw_rct.centery = random.randint(0,drawx-100), random.randint(0,drawy-50)

    #6
    vx,vy = 1, 1

    clock = pg.time.Clock()
    #2
    while True:  
        scrn_sfc.blit(bg_sfc, bg_rct)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key ==pg.K_F1:  #リセットボタン
                number = random.randint(0,9)
                file = f"fig/{number}.png"  #追加機能　画像ランダム選出
                main(file)
                return
            if event.type == pg.KEYDOWN and event.key ==pg.K_F2: #追加機能　爆弾サイズ変更
                num = random.randint(2,8)  #サイズ　ランダム
                main("fig/6.png",num)
                return

        #4
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            tori_rct.centery -= 1
        if key_lst[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_lst[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_lst[pg.K_RIGHT]:
            tori_rct.centerx += 1

        #7
        yoko, tate = check_bound(tori_rct, scrn_rct)  #符号反転
        if yoko == -1:
            if key_lst[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_lst[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_lst[pg.K_UP]:
                tori_rct.centery += 1
            if key_lst[pg.K_DOWN]:
                tori_rct.centery -= 1
            
        scrn_sfc.blit(tori_sfc,tori_rct)

        #7
        yoko, tate = check_bound(draw_rct, scrn_rct)  #符号反転
        vx *= yoko
        vy *= tate
        draw_rct.move_ip(vx,vy)
        scrn_sfc.blit(draw_sfc,draw_rct)

        #8
        if tori_rct.colliderect(draw_rct):
            ed = datetime.datetime.now()
            tkobj(st,ed)
            main()
            return
            

        pg.display.update()
        clock.tick(1000)




if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()