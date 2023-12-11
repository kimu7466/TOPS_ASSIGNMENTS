# Q.21 Write a Python function to reverses a string if its length is a multiple of 4.

# str=input("Enter the String :")
str="abcdABCD"
if len(str) % 4 == 0:
   print(''.join(reversed(str)))
   
else:
	print(str)  

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.22 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 

# string = "imroz khan"

# new_string = string[:2] + string[-2:]

# print("Input string =", string)
# print("New String =", new_string)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.23 Write a Python function to insert a string in the middle of a string.

# test_str = input("Enter main string: ")

# print("The original string is : " + str(test_str))

# mid_str = input("Enter the string to be inserted: ")

# temp = test_str.split()
# mid_pos = len(temp) //2

# res = ' '.join(temp[:mid_pos] + [mid_str] + temp[mid_pos:])

# print("Formulated String : " + str(res))
