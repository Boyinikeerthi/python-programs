name="anudip"
print(name)
print(name[0])
print(len(name))

val=input("Enter course name")
print(val)
print('pyt'in val)

#String inmutability
name='python'
print(id(name))
name1='java'
print(name+name1)
print(" "*3,name1)
print(name[5])

#formatting
str="India {0:s} and value is {1:4.2f}".format("currency",0.75123)
print(str)

#string formatting
str1="price"
cost=200.98
count=5
str="mango %s for kg is %4.2f"%(str1,cost)
print(str)
print("mango %s for kg is %8.2f and count is %3d"%(str1,cost,count))

#string Slicing:
str="Python Programming"
print(str[2:7])
print(str[ :10])
print(str[4:])
print(str[::2])
print(str[::-1])
for i in str:
    print(i)
