print("hello")
'''
import os
if os.path.exists("project.py"):
    os.remove("project.py")
else:
    print("dont talk rubbish")
'''
#program to generate MD5 of string data
import hashlib                       #its an library which is used to has
                                     #the text in one way
print(hashlib.algorithms_available) #it will print the name of algorithm
                                     # in available in hahlib
txt=input("enter the string")
m=hashlib.md5()
m.update(txt.encode('utf-8'))
print("Your String  is: "+txt+"\nkmd5 of string data is",m.hexdigest())                  #it will print the md5 of string data