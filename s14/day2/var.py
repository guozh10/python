# -*- coding:utf8 *-*
#guozhenhui

'''import sys
print (sys.path)
print (sys.argv)'''
import os
cmd = os.system('dir')
cmd_s = os.popen("dir").read()   #保存系统命令输出的结果给变量

print ("os.system",cmd_s)