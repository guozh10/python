# -*- coding:utf-8 -*-
# guozhenhui
name = 'my is guozhenhui'
name1 = 'My is\t guozhenhui'
name2 = 'My is {name} year {year}'

#首字母大写
print(name.capitalize())
#统计在字符串中的个数
print(name.count('h'))
#在字符串中不够50拿’-‘左右补
print(name.center(50,'-'))
#判断以hui结尾.......邮件地址最常用
print(name.endswith('hui'))
#在字符串中有TAB键 添加多少个空格
print(name1.expandtabs(tabsize=40))
print(name1)
#查找字符在字符串的位置，字符串切片
print(name[name.find('zhen'):])
#格式化参数
print(name2.format(name='guozhenhui',year='23'))
print(name2.format_map({'name':'guozhenhui','year':23}))
#‘guo’在字符串中的位置
print(name.index('guo'))
#判断在字符串中是否有特殊符号
print('abc23'.isalnum())
#判断是否字母
print('abcA'.isalpha())

print('122'.isdecimal())
print('122'.isdigit())
#判断是不是一个合法的变量名
print('name'.isidentifier())
#在字符串中是否是数字
print('33'.isnumeric())
#是否是空格
print(' '.isspace())
#判断首字母是不是大写
print('My Name Is'.istitle())
#把列表拼成字符串
name3 = ['guo','zhen','hui']
print('+'.join(name3))
#字符串长度不够50个在尾部补全
print(name.ljust(50,'*'))
#字符串长度不够50个在首部补全
print(name.rjust(50,'!'))
#把大写边小写
print('Guo'.lower())
#把小写变大写
print('Guo'.upper())
#去掉左空行
print('\nguo')
print('\nGuo'.lstrip())
#去掉右空行
print('guo\n'.rstrip())
#去掉左右空行
print('     guozhenhui\n'.strip())
#替换
print('guozhenhui'.replace('g','G',1))
print('guozhenhui'.rfind('h'))
#把字符串变成列表
print('guo zhen hui'.split())
print('1+2+3+4'.split('+'))
print('1+2+3+4'.split('+'))


