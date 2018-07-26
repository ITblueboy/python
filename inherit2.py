# coding:utf-8
class Parent(object):
    def Func(self):
        print "This is a parent"


class Child(Parent):
    def Func(self):
        print "This is a Child"


p = Parent()
p.Func()
c = Child()
c.Func()
