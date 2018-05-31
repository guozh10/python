# -*- coding:utf-8 -*-
# guozhenhui

import getpass
_user = "lisi"
_password = "abc123"
username = input("username:")
#password = getpass.getpass("password:")
password = input("password:")
#print(username,password)
if _user == username and _password == password:
    print ("welcom user {name} login".format(name=username))
else:
    print ("Invalid username or password")