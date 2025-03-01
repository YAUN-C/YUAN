import random
import time

harmful_waste = ["废电池", "过期药品", "杀虫喷雾罐", "打印机墨盒", "旧电子产品"]
kitchen_waste = ["菜叶", "剩菜", "剩饭", "果皮", "剩下的蛋糕", "鸡心", "鸭血", "落叶", "枯萎的草", "坏掉的树根"]
other_waste = ["砖瓦陶瓷", "渣土", "收据发票", "碎陶片", "贝壳", "烟头", "烟灰"]
recoverable_waste = ["衣服", "牛奶纸盒", "报纸", "纸箱子", "泡沫塑料", "矿泉水瓶", "可乐罐"]

harmful_waste2 = ["染发剂壳", "日光灯管", "水银体温计", "硒鼓", "除草剂容器", "油漆桶", "灯泡"]
kitchen_waste2 = ["蛋壳", "茶渣", "骨头", "过期的食用油", "落花", "鹅肝", "牛肚", "猪肺", "西瓜皮"]
other_waste2 = ["卫生间废纸", "瓷器碎", "照片", "一次性餐具", "受污染的玻璃", "受污染的塑料制品", "灰土"]
recoverable_waste2 = ["塑料玩具", "旧毛巾", "玻璃饮料瓶", "镜片", "易拉罐", "金属罐头盒", "金戒指"]
wrong_list = []

while True:
    choice = input('''请输入选项: 
            s. 开始玩游戏
            u. 升级难度
            q. 结束游戏\n''')
    if choice == "s":
        print("\033c")
        score = 0
        while score < 10 and len(wrong_list) < 5:
            print()
            waste_type = random.randint(1, 4)
            if waste_type == 1:
                wt = "有害垃圾"
                question = random.choice(harmful_waste)
                harmful_waste.remove(question)
            elif waste_type == 2:
                wt = "厨余垃圾"
                question = random.choice(kitchen_waste)
                kitchen_waste.remove(question)
            elif waste_type == 3:
                wt = "其它垃圾"
                question = random.choice(other_waste)
                other_waste.remove(question)
            elif waste_type == 4:
                wt = "可回收垃圾"
                question = random.choice(recoverable_waste)
                recoverable_waste.remove(question)
            print("请将【%s】分类：\n\t1.有害垃圾    \n\t2.厨余垃圾    \n\t3.其它垃圾    \n\t4.可回收垃圾" % question)
            ans = int(input("请输入你的选择："))
            if ans == waste_type:
                score += 2
                print("✅  哇，恭喜你！答对了！！！(oﾟ▽ ﾟ)o  当前积分为 %d分" % score)
            else:
                wrong_list.append("【%s】是【%s】" % (question, wt))
                score -= 1
                print("⛔  很可惜，差点就对了~┗|｀O′|┛ 【%s】是《%s》，已将【%s】加入错题本。" % (question, wt, question))
        if len(wrong_list) > 0:
            print("🔥 游戏结束 🔥")
            time.sleep(2)
            print("\033c\n\n\n")
            print("✍  回顾时刻 ✍")
            print("🔖 你错了 %d 题，你还记得是啥不？٩(๑❛ᴗ❛๑)۶" % len(wrong_list))
            for w in wrong_list:
                print("☞ %s☑" % w)
            wrong_list.clear()
    elif choice == "u":
        print("正在扩充题库......")
        # 进度条
        for i in range(101):
            print(f"\r[{i:3}%" + "==" * (i // 10 + 1) + ">]", end="")
            time.sleep(0.05)
        # 将harmful_waste2列表中的内容扩展至harmful_waste中
        harmful_waste.extend(harmful_waste2)
        # 将kitchen_waste2列表中的内容扩展至kitchen_waste中
        kitchen_waste.extend(kitchen_waste2)
        # 将other_waste2列表中的内容扩展至other_waste中
        other_waste.extend(other_waste2)
        # 扩展recoverable_waste列表的内容
        recoverable_waste.extend(recoverable_waste2)
        print()
        print("(ﾉﾟ▽ﾟ)ﾉ题库扩充完成！快开始挑战吧！")
        for i in range(3, 1, -1):
            print(f"\r开始倒计时：{i}", end="")
            time.sleep(1)
        print("\033c")
        # print("更新后，垃圾种类是: ")
        # print("【有害垃圾】为：%s" % harmful_waste)
        # print("【厨余垃圾】为：%s" % kitchen_waste)
        # print("【其他收垃圾】为：%s" % other_waste)
        # print("【可回收垃圾】为：%s" % recoverable_waste)
    elif choice == "q":
        print("\033c")
        print("游戏结束了~❣")
        break
    else:
        print("错误选项，请重新输入！ヽ(`Д´)ﾉ")