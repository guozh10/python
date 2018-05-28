# -*- coding:utf-8 -*-
# guozhenhui

name = input("name:")
job =input("job:")

list = '''
---------------- info list %s--------------
name:%s
job:%s
'''%(name,name,job)
print (list)

list2 ='''
-------------------info list2 fo {_Name} ----------
name:{_Name}
job:{_Job}
'''.format(_Name=name,
            _Job=job)
print (list2)