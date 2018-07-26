# coding:utf-8
class Parent(object):
    def __init__(self):
        self.x = 100


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.y = 200


p = Parent()
print p.x
c = Child()
print c.x
print c.y
