try:    
    a=int(input("entera number"))
    b=int(input("entera number"))
    print(b)
    if b==0:
        raise ("B value zero")
    else:
        c=a/b
        print(c)
except TypeErrorExceptionr as e:
    print(e)

