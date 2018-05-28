# -*- coding:utf-8 -*-
# guozhenhui
conut =0
age = 56
#任性玩，如果执行3次不对，继续按回车，不玩按n
while conut < 3:
    guest_age = int(input("age:"))
    if guest_age ==age:
        print("yes you got it")
        break
    elif guest_age > age:
        print("think smaller...")
    else:
        print("think bigger")
    conut +=1
    if conut ==3:
        conut_continue = input("do you want to keep guessing..?")
        if conut_continue !="n":
            conut =0
