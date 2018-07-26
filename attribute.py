# coding:utf-8
class Animal(object):
    name = "tiger"


print hasattr(Animal, 'name')
print getattr(Animal, 'name')
print setattr(Animal, 'name', 'lion')
delattr(Animal, 'name')
