# coding:utf-8
class Apple(object):
    name = "apple"

    @classmethod
    def myprint(cls):
        print cls.name


a = Apple()
a.myprint()
