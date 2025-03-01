from tkinter import *
import os.path

filename = 'students.txt'


def main():
    while True:
        root()
        choice = int(input('请选择功能'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print("欢迎您的使用！！")
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
        input()
def ini():
      Lstbox1.delete(0,END)
      list_items = ["一班","二班","三班","四班","五班","六班","..."]
      for item in list_items:
           Lstbox1.insert(END,item)

def clear():
      Lstbox1.delete(0,END)

def ins():
      if entry.get() != '':
          if Lstbox1.curselection() == ():
              Lstbox1.insert(Lstbox1.size(),entry.get())
          else:
              Lstbox1.insert(Lstbox1.curselection(),entry.get())

def updt():
      if entry.get() != '' and Lstbox1.curselection() != ():
           selected=Lstbox1.curselection()[0]
           Lstbox1.delete(selected)
           Lstbox1.insert(selected,entry.get())

def delt():
      if Lstbox1.curselection() != ():
           Lstbox1.delete(Lstbox1.curselection())

root = Tk()
root.title('列表框')
root.geometry('600x500')

frame1 = Frame(root,relief=RAISED)
frame1.place(relx=0,rely=0.2,relheight=0.8,relwidth=0.3)
txt = Text(root)
txt.place(relx=0.02,rely=0.7, relheight=0.2)

frame2 = Frame(root,relief=GROOVE)
frame2.place(relx=0.74,rely=0.2,relheight=0.5)

Lstbox1 = Listbox(frame1)
Lstbox1.pack()
entry = Entry(frame2)
entry.pack()
lb1 = Label(root, text='=================学生信息管理系统==================='
                       '\n===============功能菜单==================',
            font=('SDK_SC_Web',18,'bold'))
lb1.place(relx=0.0, rely=-0.02, relwidth=1, relheight=0.2)

btn1 = Button(frame2,text='显示所有班级',command=ini)
btn1.pack(fill=X)

btn2 = Button(frame2,text='录入学生信息',command=ins)
btn2.pack(fill=X)

btn3 = Button(frame2,text='查找学生信息',) # 添加和插入功能实质上是一样的
btn3.pack(fill=X)

btn4 = Button(frame2,text='修改学生信息',command=updt)
btn4.pack(fill=X)

btn5 = Button(frame2,text='统计学生总人数',command=delt)
btn5.pack(fill=X)

btn6 = Button(frame2,text='删除学生信息',command=clear)
btn6.pack(fill=X)

root.mainloop()