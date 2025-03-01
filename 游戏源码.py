import os

# 学生系统基本功能
# 增删查改

# 如何实现该系统
# 1.显示系统功能界面
# 2.让用户选择功能
# 3.判断用户选择的指定功能，然后完成相应的操作（增删查改）

# 面向对象分析
# 1.抽象类
# 学生系统管理类  学生类
# 2.分析类的成员

# 学生系统管理类
# 属性：学生列表属性 保存学生信息
# 方法：添加学生 删除学生 显示学生信息等这些方法

# 学生类
# 属性：姓名 年龄 性别
# 方法：无
class Student(object):
    def __init__(self,name,age,sex):
        # 添加相关的属性信息
        self.name=name
        self.age=age
        self.sex=sex



class StudentManageSystem(object):
    def __init__(self):
        # 定义一个列表用于保存学生对象
        self.student_list = list()


    # 将功能代码放到指定函数里面
    def show_menu(self):
        '''该函数是为了展示功能界面'''
        # 1. 显示系统的功能菜单
        print("------学生管理系统1.0------")
        print("1.添加学生信息")
        print("2.修改学生信息")
        print("3.删除学生信息")
        print("4.显示所有学生")
        print("5.查询学生信息")
        print("6.退出管理系统")


    # 添加学生函数
    # 分析：
    # 1. 学生的信息如何表示？
    # 2. 管理系统里面的学生信息如何表示？
    def add_student(self):
        name = input("请输入学生的姓名:")
        age = input("请输入学生的年龄:")
        sex = input("请输入学生的性别:")
        # 添加一个学生，需要自己创建一个学生对象
        stu=Student(name,age,sex)
        # 把对象添加到列表里面
        self.student_list.append(stu)
        # 显示学生信息
        # print(self.student_list)
        print("添加成功")

    # 显示所有学生函数
    def show_all_student(self):
        '''该函数用于显示所有的学生信息'''
        # 注意列表里面储存的是字典
        # 遍历的时候使用enumerate函数可以返回下标
        for index, student in enumerate(self.student_list):
            # 计算学号=下标+1
            student_no = index + 1
            print("学号:", student_no,
                  "姓名:", student.name,
                  "年龄:", student.age,
                  "性别:", student.sex)


    # 修改学生信息函数
    def modify_student(self):
        ''''该函数用来修改学生信息'''
        # 1. 接收用户要修改学生的学号
        student_no = int(input("请输入要修改学生的学号:"))

        # 2. 把学号转成下标, 下标 = 学号 - 1
        index = student_no - 1
        # 判断下标是否合法
        if 0 <= index < len(self.student_list):
            # 3. 根据下标获取要修改的学生字典
            student = self.student_list[index]

            # 4. 对学生字典的数据进行修改（名字， 年龄， 性别）
            new_name = input("请输入修改后的姓名:")
            new_age = input("请输入修改后的年龄:")
            new_sex = input("请输入修改后的性别:")
            # 对字典里面的数据进行修改
            student.name = new_name
            student.age = new_age
            student.sex = new_sex

            print("修改成功")
        else:
            print("请输入正确的学号：")


    # 删除学生信息
    def delete_student(self):
        """该函数用来删除学生信息"""
        # 1.接收用户输入的学号
        student_no = int(input("请输入要删除学生的学号:"))
        # 2.将学号转换为下标
        index = student_no - 1
        # 判断下表是否合法
        if 0 <= index <= len(self.student_list):
            # 需求删除后把这个人的姓名显示出来,使用pop会把删除的内容返回
            student = self.student_list.pop(index)
            print("%s,删除成功！" % student.name)
        else:
            print("请输入有效学号！")


    # 查询某个学生信息
    def query_student(self):
        """该函数用来查询学生信息"""
        name = input("请输入要查询学生的姓名:")
        for index, student in enumerate(self.student_list):
            student_no = index + 1
            if student.name == name:
                print("学号:", student_no,
                      "姓名:", student.name,
                      "年龄:", student.age,
                      "性别:", student.sex)
                break
        # 当循环语句没有执行break，表示没有该学生信息执行else里面的语句
        # 当循环执行break语句的时候，说明该学生信息存在，不会执行else里面的语句
        # 注意：当for循环与else一起使用的时候，如果没有执行for循环里面的break则会执行else语句！！！
        else:
            print("对不起，没有该学生")

    # 讲列表里面的数据保存到文件里面
    def save_file(self):
        # 1.打开文件 要以w方式打开
        file=open("student_list.data","w",encoding="utf-8")
        #2.把数据写入文件(把列表转换为字符串类型)
        # 把列表里面的每一个对象转换成学生列表里面的字典，把对象的属性信息保存到字典里面
        # stu.__dict__  获取学生的字典信息把对象的属性信息以字典的形式返回
        new_list=[stu.__dict__ for stu in self.student_list]
        student_list_str=str(new_list)
        print(student_list_str,type(student_list_str))
        file.write(student_list_str)
        file.close()

    # 加载文件里面的内容,将文件里面的内容加载到列表里面****

    def load_file(self):
        # 1.判断文件是否存在  返回值类型是布尔类型
        if os.path.exists("student_list.data"):
            # 1.打开文件 r模式
            file=open("student_list.data","r",encoding="utf-8")
            # 2.读取文件里面的数据
            value=file.read()
            # 因为从文件里面读取的是字符串类型，所以需要先转换为列表类型
            # 注意这里将字符串转换为列表需要使用eval()函数，获取字符串包裹的内容
            new_list=eval(value)
            print("从文件里面获取的内容为:",new_list,type(new_list))
            # 把列表里面每一个学生字典信息转换为对象
            # **stu_dict:把字典里面的每一项数据按照关键字传参
            # Student(**stu_dict)表示创建一个学生对象
            new_list=[Student(**stu_dict) for stu_dict in new_list]
            print(new_list)
            # 3.将文件里面的内容添加到列表里面
    #         方法一：使用global
    #         global student_list
    #         student_list=new_list
    #         方法2：方式，把文件中的列表数据扩展到全局变量里面, 这里不需要加上global，因为列表是可变类型
            self.student_list.extend(new_list)
            file.close()


    # 程序入口函数，程序开始时第一个执行的函数
    def start(self):
        # 当程序运行的时候加载一次文件
        self.load_file()

        while True:
            # 1.显示系统功能菜单
            self.show_menu()

            # 2.接收用户输入的功能选项
            menu_option = input("请输入你要操作的功能选项：")

            # 3. 判断用户选择的指定功能，然后完成对应的操作（增删改查的功能）
            if menu_option == "1":
                print("添加学生信息")
                self.add_student()
            elif menu_option == "2":
                print("修改学生信息")
                self.modify_student()
            elif menu_option == "3":
                print("删除学生信息")
                self.delete_student()
            elif menu_option == "4":
                print("显示学生信息")
                self.show_all_student()
            elif menu_option == "5":
                print("查询学生信息")
                self.query_student()
            elif menu_option == "6":
                print("程序退出")
                self.save_file()
                break

system=StudentManageSystem()

system.start()