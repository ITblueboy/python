import copy
list1 = [1,2,3,4,5,6]
print id(list1)
print id(list1[0])
print id(list1[1])
print id(list1[2])
print id(list1[3])
print id(list1[4])
print id(list1[5])
print "//////////"
list2 =copy.deepcopy(list1)
print id(list2)
print id(list2[0])
print id(list2[1])
print id(list2[2])
print id(list2[3])
print id(list2[4])
print id(list2[5])
print "//////////"
list2[0]=7
list2[1]=8
list2[2]=9
list2[3]=10
list2[4]=11
list2[5]=12
print id(list2)
print id(list2[0])
print id(list2[1])
print id(list2[2])
print id(list2[3])
print id(list2[4])
print id(list2[5])
print "//////////"
print list1
print list2
