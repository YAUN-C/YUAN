import tkinter
import random

win = tkinter.Tk()
win.title('课堂点名随机抽取产生器')
win.geometry('350x300')

num = tkinter.StringVar()
num.set('0')

label = tkinter.Label(win, textvariable=num, font=("Arial", 64))
label.place(x=135, y=30)
button = tkinter.Button(win, text="随机点名", font=("Microsoft Yahei",28), command=lambda: num.set(str(random.randint(1, 51))))
button.place(x=80, y=150, width=190, height=80)

win.mainloop()