from tkinter import *
from tkinter  import  *


def newwind():
      winNew = Toplevel(root)
      winNew.geometry('650x450')
      winNew.title('计算器')

      def run1():
          a = float(inp1.get())
          b = float(inp2.get())
          s = '计算得：%0.2f+%0.2f=%0.2f\n' % (a, b, a + b)
          txt.insert(END, s)  # 追加显示运算结果
          inp1.delete(0, END)  # 清空输入
          inp2.delete(0, END)  # 清空输入

      def run2(x, y):
          a = float(x)
          b = float(y)
          s = ('计算得：%0.2f-%0.2f=%0.2f\n' % (a, b, a - b))
          txt.insert(END, s)  # 追加显示运算结果
          inp1.delete(0, END)  # 清空输入
          inp2.delete(0, END)  # 清空输入

      def run3():
          a = float(inp1.get())
          b = float(inp2.get())
          s = '计算得：%0.2fX%0.2f=%0.2f\n' % (a, b, a * b)
          txt.insert(END, s)  # 追加显示运算结果
          inp1.delete(0, END)  # 清空输入
          inp2.delete(0, END)  # 清空输入

      def run4():
          a = float(inp1.get())
          b = float(inp2.get())
          s = '计算得：%0.2f/%0.2f=%0.2f\n' % (a, b, a / b)
          txt.insert(END, s)  # 追加显示运算结果
          inp1.delete(0, END)  # 清空输入
          inp2.delete(0, END)  # 清空输入

      btClose = Button(winNew, text='回到主页', command=winNew.destroy)
      btClose.place(relx=0.83, rely=0.8)

      lb1 = Label(winNew, text='请输入两个数，按下面四个按钮之一进行计算',font=('SDK_SC_Web',18,'bold'))
      lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
      inp1 = Entry(winNew)
      inp1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)
      inp2 = Entry(winNew)
      inp2.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.1)

      # 方法-直接调用 run1()
      btn1 = Button(winNew, text='加法', command=run1)
      btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

      # 方法二利用 lambda 传参数调用run2()
      btn2 = Button(winNew, text='减法', command=lambda: run2(inp1.get(), inp2.get()))
      btn2.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)

      # 方法三 乘法
      btn3 = Button(winNew, text='乘法', command=run3)
      btn3.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.1)
      # 方法四 除法
      btn4 = Button(winNew, text='除法', command=run4)
      btn4.place(relx=0.6, rely=0.6, relwidth=0.3, relheight=0.1)

      txt = Text(winNew)
      txt.place(relx=0.1,rely=0.75, relheight=0.2,relwidth=0.71)

      def newind0():
          winNew0=Toplevel(newwind)
          mainmenu = Menu(newwind)
          menuFile = Menu(mainmenu)
          mainmenu.add_cascade(label='菜单', menu=menuFile)





def newwind2():
    winNew2 = Toplevel(root)
    winNew2.geometry('460x340')
    winNew2.title('摄氏度转换工具')
    btClose = Button(winNew2, text='关闭',font=('SDK_SC_Web',12,'bold'), command=winNew2.destroy)
    btClose.place(relx=0.1, rely=0.605, relwidth=0.3, relheight=0.1 )

    def run1():
        C = float(inp1.get())
        F = (C * 9) / 5 + 32
        J = '%.1f华氏度 = %.1f摄氏度\n' % (F, C)
        txt.insert(END, J)
        inp1.delete(0, END)  # 清空输入

    def run2():
        C = float(inp1.get())
        F = (C - 32) * 5 / 9
        J = '%.1f摄氏度=%.1f华氏度\n' % (F, C)
        txt.insert(END, J)
        inp1.delete(0, END)  # 清空输入

    lb1 = Label(winNew2, text='请输入温度', font=('SDK_SC_Web',18,'bold'))
    lb1.place(relx=0.1, rely=0.05, relwidth=0.3, relheight=0.2)
    lb2 = Label(winNew2, text='温度转换：', font=('SDK_SC_Web',18,'bold'))
    lb2.place(relx=0.5, rely=0.05, relwidth=0.3, relheight=0.2)
    inp1 = Entry(winNew2)
    inp1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.16)

    # 直接调用 run1()
    btn1 = Button(winNew2, text='华氏度转摄氏度' , font=('SDK_SC_Web',12,'bold'), command=run1)
    btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)
    # 直接调用 run2()
    btn2 = Button(winNew2, text='摄氏度转华氏度' , font=('SDK_SC_Web',12,'bold'),  command=run2)
    btn2.place(relx=0.1, rely=0.51, relwidth=0.3, relheight=0.1)

    txt = Text(winNew2)
    txt.place(relx=0.5,rely=0.2, relheight=0.6,relwidth=0.45)

# 其他
def newwind3():
    winNew3 = Toplevel(root)
    winNew3.geometry('460x340')
    winNew3.title('其他')
    





# 游戏
def newwind4():
    winNew4 = Toplevel(root)
    winNew4.geometry('500x500')
    winNew4.title('游戏')
    lb = Label(winNew4, text='欢迎游玩，按回车键开始！',font=('SDK_SC_Web',20,'bold'))
    lb.place(relx=0.1,rely=0.1,relwidth=0.7,relheight=0.3)
    btClose = Button(winNew4, text='关闭',font=('SDK_SC_Web',15,'bold'), command=winNew4.destroy)
    btClose.place(relx=0.48, rely=0.9)
    btClose = Button(winNew4, text='开始',font=('SDK_SC_Web',15,'bold'), command=winNew4.destroy)
    btClose.place(relx=0.36, rely=0.9)
    # 游戏代码







root = Tk()
root.title('工具1.0')
root.geometry('750x600')

lb1 = Label(root,text='欢迎使用,\n本工具',font=('SDK_SC_Web',48,'bold'))
lb1.place(relx=0.3,rely=0.2)

mainmenu = Menu(root)
menuFile = Menu(mainmenu)
mainmenu.add_cascade(label='菜单',menu=menuFile)
menuFile.add_command(label='计算器',command=newwind)
menuFile.add_separator()
menuFile.add_command(label='摄氏度',command=newwind2)
menuFile.add_separator()
menuFile.add_command(label='其他',command=newwind3)
menuFile.add_separator()
menuFile.add_command(label='游戏',command=newwind4)
menuFile.add_separator()
menuFile.add_command(label='退出',command=root.destroy)

root.config(menu=mainmenu)
root.mainloop()