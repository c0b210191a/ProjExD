import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    #tkm.showinfo(txt,f"[{txt}]ボタンが押された")
    entry.insert(tk.END,txt)

def eq_click(event):
    btn = event.widget
    #txt = btn["text"]
    cal = entry.get()
    ans = eval(cal)
    entry.delete(0,tk.END)
    entry.insert(tk.END,ans)

root = tk.Tk()
root.geometry("300x600")

entry = tk.Entry(root,width=10,font=("Times New Roman",40),justify="right")
entry.grid(row=0,column=0,columnspan=3)

#------------------------------------------------------------------------
r = 1
c = 0
num = list(range(9,-1,-1))
ope = ["+"]
for i,n in enumerate(num+ope,1):
    button = tk.Button(root,text=f"{n}",font=("Times New Roman",30),width=4,height=2)
    button.bind("<1>",button_click)
    button.grid(row=r,column=c)
    c += 1
    if i%3 == 0:
        r+=1
        c = 0
#------------------------------------------------------------------------
button = tk.Button(root,text="=",font=("Times New Roman",30),width=4,height=2)
button.bind("<1>",eq_click)
button.grid(row=4,column=2)

#entry.get()


root.mainloop()