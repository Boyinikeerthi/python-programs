str="p@#yn26at^&i5ve"
charcount,digitcount,symbolcount=0,0,0
for s in str:
    if s.isalpha():
        charcount+=1
    elif s.isdigit():
        digitcount+=1
    else:
        symbolcount+=1
print(f"digitcount={digitcount},charcount={charcount},symbolcount={symbolcount}")

""""
#file handling
file=open("strings.py","r")
for line in file:
          print(line)
file.close()
"""""

file=open("strings.py","w")
if file:
    print("file opened")
file.write("python is a interpreted program")
file.close()
