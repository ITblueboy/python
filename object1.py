# coding:utf-8
class Animal(object):
    def Init(self):
        self.animal = "tiger"

    def myprintf(self):
        print self.animal


a = Animal()
a.Init()
a.myprintf()
