#program to reverse the words

str="Data Analysis using python"
list2=str.split()[::-1]
str2=" ".join(list2)
print(str2)


#total length of a string

str1="i am keerthi"
print(len(str1))



#length of ech word in the string

str="data analysis using python"
list3=str.split()
for n in list3:
    print(n,"=",len(n))


#Count of each vowel present in the given string 

str="data analysis using python"
a_count = e_count = i_count = o_count = u_count = 0
for char in str:
    if char == 'a':
        a_count += 1
    elif char == 'e':
        e_count += 1
    elif char == 'i':
        i_count += 1
    elif char == 'o':
        o_count += 1
    elif char == 'u':
        u_count += 1

print("A:", a_count, "E:", e_count, "I:", i_count, "O:", o_count, "U:", u_count)

