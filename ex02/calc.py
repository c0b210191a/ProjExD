import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):    #ボタンを押すと文字が入力される関数
    btn = event.widget  #
    txt = btn["text"]
    entry.insert(tk.END,txt)

def eq_click(event):    #ボタンを押すと計算結果が出力される関数
    btn = event.widget
    cal = entry.get()
    ans = eval(cal)
    entry.delete(0,tk.END)
    entry.insert(tk.END,ans)

def del_click(event):   #ボタンを押すと文字がすべて消える関数
    btn = event.widget
    entry.delete(0,tk.END)

def back_click(event):  #ボタン押すと後ろの文字が消える関数
    btn = event.widget
    cal = len(entry.get())-1
    entry.delete(cal,tk.END)

# def his_click(event):
#     btn = event.widget

root = tk.Tk()
root.title("電卓")
root.geometry("390x660")

entry = tk.Entry(root,width=10,font=("Times New Roman",20),justify="right")
entry.grid(row=0,column=0,columnspan=4)

#------------------------------------------------------------------------
r = 1
c = 0
num = list(range(9,-1,-1))
ope = ["+","-","*","/","**"]     #四則演算と二乗
for i,n in enumerate(num+ope,1):
    button = tk.Button(root,text=f"{n}",font=("Times New Roman",30),width=4,height=2)
    button.bind("<1>",button_click)     #左クリックで関数を呼び出す
    button.grid(row=r,column=c)     #ボタンの配置位置を決める
    c += 1
    if i%3 == 0:
        r+=1
        c = 0
#------------------------------------------------------------------------
button = tk.Button(root,text="=",font=("Times New Roman",30),bg="lightskyblue",width=4,height=2)    #計算結果を出力する
button.bind("<1>",eq_click)     #左クリックで関数を呼び出す
button.grid(row=3,column=3)     #ボタンの配置位置を決める

button = tk.Button(root,text="del",font=("Times New Roman",30),bg="aliceblue",width=4,height=2) #文字を全て消す
button.bind("<1>",del_click)     #左クリックで関数を呼び出す
button.grid(row=1,column=3)     #ボタンの配置位置を決める

button = tk.Button(root,text="🔙",font=("Times New Roman",30),bg="aliceblue",width=4,height=2)  #直前に入力された文字を消す
button.bind("<1>",back_click)     #左クリックで関数を呼び出す
button.grid(row=2,column=3)     #ボタンの配置位置を決める

# button = tk.Button(root,text="履歴",font=("Times New Roman",30),bg="aliceblue",width=4,height=2)  #直前に入力された文字を消す
# button.bind("<1>",his_click)     #左クリックで関数を呼び出す
# button.grid(row=3,column=3)     #ボタンの配置位置を決める

root.mainloop()