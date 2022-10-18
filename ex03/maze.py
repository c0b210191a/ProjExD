import tkinter as tk
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

def key_up():
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "Up":
        cy -=20
    elif key =="Down":
        cy +=20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20
    
    canvas.coords("こうかとん",cx,cy)
    root.after(1000,main_proc)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #1
    
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack() #2

    tori = tk.PhotoImage(file="fig/6.png")
    cx, cy = 300, 400
    canvas.create_image(cx,cy,image=tori,tag="こうかとん") #3

    key = "" #4

    root.bind("<KeyPress>",key_down) #5

    root.bind("<KeyRelease>",key_up) #6


    main_proc() #7

    root.mainloop() 