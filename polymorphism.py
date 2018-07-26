# coding:utf-8
class Fruit(object):
    def myprint(self):
        print "This is a Fruit"


class Apple(Fruit):
    def myprint(self):
        print "This is a Apple"


def Func(Fruit):
    Fruit.myprint()


f = Fruit()
Func(f)
a = Apple()
Func(a)
