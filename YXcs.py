from tkinter import *
import tkinter.messagebox

def xz():
    answer=tkinter.messagebox.askokcancel('请选择','请选择确定或取消')
    if answer:
        lb.config(text='已确认')
    else:
        lb.config(text='已取消')

root = Tk()
root.geometry('500x450')

lb = Label(root,text='')
lb.pack()
btn=Button(root,text='弹出对话框',command=xz)
btn.pack()
root.mainloop()
from tkinter.simpledialog import *

def xz():
    s=askstring('请输入','请输入一串文字')
    lb.config(text=s)

root = Tk()
root.geometry('240x180')

lb = Label(root,text='')
lb.pack()
btn=Button(root,text='弹出输入对话框',command=xz)
btn.pack()
root.mainloop()