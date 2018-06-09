# -*- coding:utf-8 -*-
# guozhenhui 
'''              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
'''
prodcut_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Alex Python',120)
]
shopping_list = []
salary = input('input your salary:')
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,time in enumerate(prodcut_list):
            print(index,time)
        user_choice = input('选择要买啥:')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(prodcut_list) and user_choice >=0:
                p_time = prodcut_list[user_choice]
                if p_time[1] <= salary:
                    shopping_list.append(p_time)
                    salary -= p_time[1]
                    print('added %s into shopping cart, your current balance is \033[32;1m%s\033[0m'%(p_time,salary))
                else:
                    print("\033[41;1m你的余额剩余[%s] 还买个毛线呢！\033[0m"%salary)
            else:
                print('\033[41;1mproduct code [%s] is not exst!\033[0m'%user_choice)
        elif user_choice == 'q':
            print("------------shopping list--------------")
            for p in shopping_list:
                print(p)
            print('your current balance:',salary)
            exit()
        else:
            print('\033[41;1minvalid option\033[0m')