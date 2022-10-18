import tkinter as tk
import maze_maker as mm
import random
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key == "Up":
        my -=1
    if key =="Down":
        my +=1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1

    if m_list[my][mx] == 0:
        cx, cy = mx*100+50, my*100+50
    else:
        if key == "Up":
            my +=1
        if key =="Down":
            my -=1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
        tkm.showinfo("危険","進めません") #メッセージボックス追加

    canvas.coords("こうかとん",cx,cy)
    root.after(80,main_proc) #数値変更




if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #1
    
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack() #2

    m_list = mm.make_maze(15,9) #9

    mm.show_maze(canvas,m_list) #10

    file_random = f"fig/{random.randint(0,9)}.png"  #画像ランダム化
    tori = tk.PhotoImage(file=file_random)
    mx, my =1,1
    cx, cy = 300, 400
    canvas.create_image(cx,cy,image=tori,tag="こうかとん") #3

    key = "" #4

    root.bind("<KeyPress>",key_down) #5

    root.bind("<KeyRelease>",key_up) #6

    
    main_proc() #7

    

    root.mainloop() 