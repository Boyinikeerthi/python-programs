try:    
    file=open("exception.py","r")
    for line in file:
        print(line)
except:
    print("File not found")
else:
    print("else block")
finally:
    file.close()
    print("finally")
