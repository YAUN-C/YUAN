from tkinter import *

def run1():
     a = float(inp1.get())
     b = float(inp2.get())
     s = '%0.2f+%0.2f=%0.2f\n' % (a,b, a+b)
     txt.insert(END, s)   # 追加显示运算结果
     inp1.delete(0, END)  # 清空输入
     inp2.delete(0, END)  # 清空输入

def run2(x, y):
     a = float(x)
     b = float(y)
     s = '%0.2f-%0.2f=%0.2f\n' % (a,b, a-b)
     txt.insert(END, s)   # 追加显示运算结果
     inp1.delete(0, END)  # 清空输入
     inp2.delete(0, END)  # 清空输入

def run3():
     a = float(inp1.get())
     b = float(inp2.get())
     s = '%0.2fX%0.2f=%0.2f\n' % (a,b, a*b)
     txt.insert(END, s)   # 追加显示运算结果
     inp1.delete(0, END)  # 清空输入
     inp2.delete(0, END)  # 清空输入

def run4():
     a = float(inp1.get())
     b = float(inp2.get())
     s = '%0.2f/%0.2f=%0.2f\n' % (a,b, a/b)
     txt.insert(END, s)   # 追加显示运算结果
     inp1.delete(0, END)  # 清空输入
     inp2.delete(0, END)  # 清空输入

root = Tk()
root.geometry('800x450')
root.title('简单计算器')
lb = Label(root,text='欢迎使用',\
        bg='#0066FF',\
        font=('SDK_SC_Web',48),\
        width=8,\
        height=4,\
        relief=SUNKEN)
lb.pack()

lb1 = Label(root, text='请输入两个数，按下面四个按钮之一进行计算')
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
inp1 = Entry(root)
inp1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)
inp2 = Entry(root)
inp2.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.1)


# 方法-直接调用 run1()
btn1 = Button(root, text='加法', command=run1)
btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

# 方法二利用 lambda 传参数调用run2()
btn2 = Button(root, text='减法', command=lambda: run2(inp1.get(), inp2.get()))
btn2.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)

# 方法三 乘法
btn3 = Button(root, text='乘法', command=run3)
btn3.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.1)
# 方法四 除法
btn4 = Button(root, text='除法',command=run4)
btn4.place(relx=0.6, rely=0.6, relwidth=0.3, relheight=0.1)
# 在窗体垂直自上而下位置80%处起，布局相对窗体高度20%高的文本框
txt = Text(root)
txt.place(rely=0.8, relheight=0.2)

root.mainloop()