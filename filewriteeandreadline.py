name = input("Enter your name: ")
age = input("Enter your age: ")

with open("data.txt", "w") as file:
    file.write(name + "\n")
    file.write(age)




with open("data.txt", "r") as file:
    name = file.readline().strip()
    age = file.readline().strip()

print(f"Welcome {name} and {age}")
