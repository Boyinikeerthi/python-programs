#global and local variables
def  product(a,b):
    global x
    x=a*b
    print("product", x)
x=10
print(x)
product(30,40)
print(x)
