# coding:utf-8
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = raw_input()


def Find(a, x):
    print(len(a))
    for i in range(0, len(a)-1):
        if a[i] == int(x):
            return i
    return None


ret = Find(a, x)
print("result:", ret)
