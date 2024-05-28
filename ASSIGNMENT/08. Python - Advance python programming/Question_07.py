# 7. Write a Python program to read a file line by line store it into a variable.

file = open('output.txt', 'r')
str_content = ""

for i in range(0,1000 ):
    char = file.read(1)  
    if char:
        str_content += char  

print(str_content)

file.close()  
 

 