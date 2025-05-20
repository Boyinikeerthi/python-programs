#if b==0
#raise ZeroDivisionException
#a/b
#raise:

a=10
b=0
try:
    if b==0:
        raise ZeroDivisionException("B value zero")
    else:
        c=a/b
        print(c)
except ZeroDivisionError as e:
    print(e)
