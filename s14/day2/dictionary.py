# -*- coding:utf-8 -*-
# guozhenhui 
date = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["lianjia","woaiwojia"]
        },
        "朝阳": {
            "望京":["奔驰","陌陌"],
            "国贸":["CICC","HP"],
            "东直门":["Advent","飞信"]
        },
        "海淀":{},
    },
    "山东":{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    "广东":{
    "东莞":{},
    "佛山":{}
    },
}
exit_flag = False
while not exit_flag:
    for i in date:
        print(i)
        
    choice = input("选择进入1>>>:")
    if choice in date:
        while not exit_flag:
            for i2 in date[choice]:
                print("\t",i2)
            choice2 = input("选择进入2>>>:")
            if choice2 in date[choice]:
                while not exit_flag:
                    for i3 in date[choice][choice2]:
                        print("\t\t",i3)
                    choice3 = input("选择进入3>>>:")
                    if choice3 in date[choice][choice2]:
                        for i4 in date[choice][choice2][choice3]:
                            print("\t\t",i4)
                        choice4 = input("最后一层，按B返回>>>:")
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            exit_flag = True
                    if choice3 == "b":
                       break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True
    elif choice == "q":
        exit_flag = True
