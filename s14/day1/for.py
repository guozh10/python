# -*- coding:utf-8 -*-
# guozhenhui
age =56
for i in range(3):
    guest_age = int(input("age:"))
    if guest_age ==age:
        print("yes you got it")
        break
    elif guest_age > age:
        print("think smaller...")
    else:
        print("think bigger")
else:
    print ("you have tried too many times...fuck off")