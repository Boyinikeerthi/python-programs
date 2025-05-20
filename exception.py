#Exception handling
#try:
#statement which may rise the exception
#except:
#handle the exception
#else:
#when the exception not raised the else block will be executed
#finally:
#irrespective of the error raied or not final block will be executed

try:
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=a/b
    print(c)
    print("middle")
except ZeroDivisionError:
    print("b value cannot be a zero")
except:
    print("value should be a number")
print("End")
