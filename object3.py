# coding:utf-8
class Animal(object):
    Name = ""
    Age = 0

    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def myprint(self):
        print self.Name
        print self.Age


a = Animal("tiger", 12)
a.myprint()
