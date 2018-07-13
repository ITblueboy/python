# coding:utf-8
target_list = []
for i in range(5):
    print "输入第%s个元素" % (i + 1)
    number = raw_input()
    num = int(number)
    target_list.append(num)
count = sum(target_list)
print count/5
