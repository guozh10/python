# -*- coding:utf8 *-*
#guozhenhui
#列表
name = ['a','b','c','d','e','dd']
#切片从0开始
print (name[1])
#位置1到3到参数，去头不取尾
print (name[1:3])
print (name[-1])
#在末尾添加一个值
name.append('e')
print ('add',name)
#插入f到位置2上
name.insert(2,'f')

print ('chadui',name)
#显示从又数第二个
name[-2] = 'D'

print ('tihuan',name)
#显示位置号并打印参数
print (name[name.index('c')])
#取值位置1的参数
print (name.pop(1))
#统计字符串在列表中有几个
print ('count',name.count('e'),name)
#清除列表)# name.clear(
#翻转数值
name.reverse()
print (name)
#排序，特殊符号、数字、大写、小写
name.sort()
print(name)

#合并列表/
name2 = [1,2,3,4]
name.extend(name2)
print(name,name2)
#删除变量
#el name2
#rint(name2)
