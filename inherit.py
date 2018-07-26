# coding:utf-8
class Parent(object):
    def Parentmethod(self):
        print "This is a parent"


class Child(Parent):
    def Childmethod(self):
        print "This is a child"


p = Parent()
p.Parentmethod()
c = Child()
c.Childmethod()
c.Parentmethod()
