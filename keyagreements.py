#key arguments
def msg(name,qualification):
    """ Welcome Function """
    print("welcome ",name, "with qualification",qualification)
msg(qualification= "MCA",name= "Anudip")


#calculation sum of 2 numbers
def add(a,b):
    return a+b
print("Result=",add(20,80))


# variable length arguments *args, **kwargs
#*args
def access(*args):
 for a in args:
    print(a)
access(12,1,23,4.5,"hello")

#inner function
def fun1():
 def fun2():
    print("Function2")
 fun2()
 print("Function1")
fun1()

        
#**Kwargs
def fun(**Kwargs):
 for key,value in Kwargs.items():
    print(key,"=",value)
fun(a=1,b=2,c=3,d=4)


#Recursion
# functiom which will call itself
#finding factorial of number
#5!=5*4*3*2*1
def factorial(num):
 if(num==1 or num==0):
        return 1
 else:
     result=num*factorial(num-1)
     return result
print(factorial(5))


#Anonmous function lmabda
#single line statement then we can se lambda function
num=lambda a:a*a
print(num(5))


#if condition operator
a=int(input("enter the number:"))
if(a%2==0):
      print("even")
else:
    print("odd")


#ternary method
a=int(input("enter the number:"))
print("even"if a%2==0 else"odd")

#method3
result = lambda a:"even" if a%2==0 else "odd"
print(result(10))



        



        





    
