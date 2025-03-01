from  tkinter import *
root = Tk()
root.title('摄氏度转换华氏度工具')
root.geometry('600x200') # 这里的乘号不是 * ，而是小写英文字母 x
lb = Label(root,text='欢迎使用',\
        bg='#0066FF',\
        font=('SDK_SC_Web',48),\
        width=30,\
        height=6,\
        relief=SUNKEN)
lb.pack()
root.mainloop()