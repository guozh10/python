# -*- coding:utf-8 -*-
# guozhenhui
conut =0
age = 56
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
else:
    print ("you have tried too many times...fuck off")