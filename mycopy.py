list1 = [1,9,2,[1,2,3]]
list2 = list1
list3 = list1[:]
list4 = list(list1)
print id(list1)
print id(list2)
print id(list3)
print id(list4)
print "////////"
print id(list1[0])
print id(list2[0])
print id(list3[0])
print id(list4[0])
print "////////"
