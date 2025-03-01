'''
摄氏度转换华氏度

型号：1.0
作者：Yuan


'''
from tkinter import *

def run1():
    C=float(inp1.get())
    F=(C*9)/5+32
    J='%.1f华氏度 = %.1f摄氏度' % (F,C)
    txt.insert(END,J)
    inp1.delete(0, END)  # 清空输入

def run2():
    C=float(inp1.get())
    F=(C-32)*5/9
    J='%.1f摄氏度=%.1f华氏度' % (F,C)
    txt.insert(END,J)
    inp1.delete(0, END)  # 清空输入

root = Tk()
root.geometry('460x240')
root.title('摄氏度转换工具')
lb1 = Label(root, text='请输入温度，按下面按钮进行计算')
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.05)
inp1 = Entry(root)
inp1.place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.1)

#直接调用 run1()
btn1 = Button(root, text='转换1', command=run1)
btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)
#直接调用 run2()
btn2 = Button(root, text='钻换2', command=run2)
btn2.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)


txt = Text(root)
txt.place(rely=0.8, relheight=0.4)

root.mainloop()