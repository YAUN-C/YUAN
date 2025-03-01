from tkinter import *
import tkinter
import random

def newwind():
    winNew = Toplevel(root)
    winNew.geometry('650x450')
    winNew.title('计算器')

# 主界面
root = Tk()
root.title('教室辅助程序0.1')
root.geometry('300x450')

#点名界面
def newwind():
    winNew = Toplevel(root)
    winNew.geometry('350x350')
    winNew.title('随机点名器1.0')
    #动画
    num = tkinter.StringVar()
    num.set('0')
    #文本框
    label = tkinter.Label(winNew, textvariable=num, font=("Arial", 64),justify='center')
    label.place(x=135, y=80)
    
    button = tkinter.Button(winNew, text="随机点名", font=("黑体",28), justify='center' ,command=lambda: num.set(str(random.randint(1, 58))))
    button.place(x=80, y=180, width=190, height=80)


#签到界面
def newwind1():
    winNew1 = Toplevel(root)
    winNew1.geometry('350x350')
    winNew1.title('学生签到系统1.0')

#积分界面
def newwind2():
    winNew2 = Toplevel(root)
    winNew2.geometry('450x450')
    winNew2.title('积分界面')

#课程表界面
def newwind3():
    winNew3 = Toplevel(root)
    winNew3.geometry('500x300')
    winNew3.title('课程表')

#设置界面
def newwind4():
    winNew4 = Toplevel(root)
    winNew4.geometry('350x300')
    winNew4.title('设置')

# 按钮A
btn1 = Button(root, text='点名',command=newwind)
btn1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)
# 按钮B
btn1 = Button(root, text='签到',command=newwind1)
btn1.place(relx=0.55, rely=0.2, relwidth=0.3, relheight=0.1)
# 按钮C
btn1 = Button(root, text='积分',command=newwind2)
btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)
# 按钮D
btn1 = Button(root, text='课程表',command=newwind3)
btn1.place(relx=0.55, rely=0.4, relwidth=0.3, relheight=0.1)


# 菜单
mainmenu = Menu(root)
menuFile = Menu(mainmenu)
mainmenu.add_cascade(label='菜单',menu=menuFile)
menuFile.add_command(label='设置',command=newwind4)
menuFile.add_separator()


root.config(menu=mainmenu)
root.mainloop()