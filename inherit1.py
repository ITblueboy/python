# coding:utf-8
class Parent(object):
    Name = "Skye"

    def Parentmethod(self):
        print self.Name


class Child(Parent):
    Age = 18

    def Childmethod(self):
        print self.Name
        print self.Age


c = Child()
c.Childmethod()
