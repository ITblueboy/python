# coding:utf-8
import random
num = random.randint(0,10000)
print (num)
while True:
    print "请输入你猜测的数字"
    number = int(raw_input())
    if number > num:
        print "太大了"
        continue
    elif number < num:
        print "太小了"
        continue
    else:
        print "恭喜你,猜对了"
        break

