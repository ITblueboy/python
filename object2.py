# coding:utf-8
class Animal(object):
    def __init__(self):
        self.animal = "tiger"

    def myprintf(self):
        print self.animal


a = Animal()
a.myprintf()
