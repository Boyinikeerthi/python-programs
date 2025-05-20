#list

list1=[10,5,6,2,8,4,4]
print(list1)
"""for i in range(len(list1)):
    print(list1[i])"""
print(list1[5])
list2=list1[:5]
print(list2)
#inserting values
list1.append("python")
print(list1)
list1.insert(1,11)
print(list1)
print(list1.index(4))
#deleting
list1.remove(4)
print(list1)
list1.pop()
print(list1)
#sorting
list1.sort(reverse=True)
print(list1)
print(sorted(list2))
print(list2)
#copying
list3=list2
print(list3)
list2.pop()
print(list2,"\n",list3)
#del list2
#list2.clear()
print(list2)
#concatenation
list4=list2+list3
print(list4)
print(list4*2)
#extend
list2.extend([5,7,2,3])
print(list2)
#listcomprehension
list3=[]
for x in range(1,11):
    list3.append(x*x)
    print(list3)
list3=[x*x for x in range(1,5)]
print(list3)

