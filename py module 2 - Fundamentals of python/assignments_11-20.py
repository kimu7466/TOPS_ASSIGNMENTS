# Q.11 Write a python program to sum of the first n positive integers.

# n = int(input("Enter Number: "))

# sum = sum(range(n+1))
# print (sum)
# print("Sum of the first", n, "Positive numbers is", sum)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.12 Write a Python program to calculate the length of a string.

# str = input("Enter a string: ")

# print(len(str))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.13 Write a Python program to count the number of characters (character frequency) in a string.  

# string = input("Enter String: ")
# lis=list(string)

# frequency =[lis.count(elements) for elements in lis]
# a = dict(zip(lis,frequency))

# print(a) 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.14 What are negative indexes and why are they used?
'''
Negative indexing is used in Python to manipulate sequence objects such as lists, arrays, strings, etc. Negative indexing retrieves elements from the end by providing negative numbers as sequence indexes.'''

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.15 Write a Python program to count occurrences of a substring in a string. 

# strings = input("Enter string: ")
# substring = input("Enter Substring: ")

# occurrence_count = sum(string.count(substring) for string in strings.split())

# print(occurrence_count)

 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.16 Write a Python program to count the occurrences of each word in a given sentence.  

# name = (input("Enter a String: "))
# name = name.lower()

# letter_counter = {}
# empty_list = []

# for ch in name:
#     if ch not in empty_list:
#         empty_list.append(ch)
        
# for unique_ch in empty_list:
#     letter_counter.setdefault(unique_ch, name.count(unique_ch))
    
# print(letter_counter)            

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.17 Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string. 

# a = input("Enter string: ")
# b = input("Enter string: ")

# print("Before Swap :",a," ",b)
# a1 = b[:2] + a[2:]
# b1 = a[:2] + b[2:]
# print("After Swap :",a1," ",b1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.18 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

# string = input("Enter a String: ")

# if len(string) < 3:
#   print(string)
  
# elif string[-3:] == 'ing':
#   print(string + 'ly')
  
# else:
#   print(string + 'ing')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.19 Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring  with 'good'. Return the resulting string.

# def not_poor(str1):
#   snot = str1.find('not')
#   spoor = str1.find('poor')
  

#   if spoor > snot and snot>0 and spoor>0:
#     str1 = str1.replace(str1[snot:(spoor+4)], 'good')
#     return str1
#   else:
#     return str1
# print(not_poor('The lyrics is not that poor!'))
# print(not_poor('The lyrics is poor!'))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.20 Write a Python function that takes a list of words and returns the length of the longest one. 

# str = input("Enter a String: ")

# word_list = str.split()

# longest_word = max(word_list, key = len)

# print("Longest word: ",longest_word)
