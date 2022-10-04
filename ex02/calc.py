import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = int(btn["text"])
    #tkm.showinfo(txt,f"[{txt}]ボタンが押された")
    entry.insert(tk.END,txt)

root = tk.Tk()
root.geometry("300x600")

entry = tk.Entry(root,width=10,font=("Times New Roman",40),justify="right")
entry.grid(row=0,column=0,columnspan=3)

r = 1
c = 0
for i,num in enumerate(range(9,-1,-1),1):
    button = tk.Button(root,text=f"{num}",font=("Times New Roman",30),width=4,height=2)
    button.bind("<1>",button_click)
    button.grid(row=r,column=c)
    c += 1
    if i%3 == 0:
        r+=1
        c = 0
button = tk.Button(root,text="+",font=("Times New Roman",30),width=4,height=2)
button.bind("<1>",button_click)
button.grid(row=4,column=1)

root.mainloop()