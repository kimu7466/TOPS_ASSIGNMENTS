# 7. Write a Python program to read a file line by line store it into a variable.

file = open('file_for_7.txt', 'r')
str_content = ""

for i in range(0,1000 ):
    char = file.read(1)  # Read one character at a time
    if char:
        str_content += char  # Append the character to the string

print(str_content)

file.close()  # Remember to close the file when done

#>>>>>>>
# old one 



# file = open('file_name.txt', 'r')
# str=""
# for i in range(0,100):
#     str=str + f.read(i)

# print(str)
