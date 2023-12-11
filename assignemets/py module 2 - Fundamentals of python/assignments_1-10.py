# Q.1 Write a Python program to check if a number is positive, negative or zero.

# num = float(input("Enter a number: "))

# if num > 0:
#     print("The number entered is positive.")
# elif num < 0:
#     print("The number entered is negative.")
# else:
#     print("The number entered is zero.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.2 Write a Python program to get the Factorial number of given number.

# x = int(input("Enter a value for factorial: "))
# y = x
# factorial = 1

# while x > 0:
#     factorial = factorial * x
#     x = x - 1

# print("The factorial of", y, "is:", factorial)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.3 Write a Python program to get the Fibonacci series of given range.

# x = int(input("enter a number to print fibonacci series : "))

# a = 0
# b = 1
# c = 0

# while c <= x :
#     print(c)

#     a = b
#     b = c
#     c = a+b

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.4 How memory is managed in Python?

'''
Python makes use of automatic memory management through garbage collection.
The garbage collector keeps track of objects and frees memory when they are no longer in use.
Python uses reference counting to manage memory, incrementing and decrementing reference counts as needed.
'''

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.5 What is the purpose continue statement in python?


'''
The continue statement in Python is used to skip the remaining code inside a loop for the current iteration only.
A continue statement ends the current iteration of a loop. Program control is passed from the continue statement to the end of the loop body.
A continue statement can only appear within the body of an iterative statement, such as do , for , or while .

'''
#Example

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in number_list:

#   if i % 2 == 0:

#     continue

#   print(i)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.6 Write python program that swap two number with temp variable and without temp variable.

# swapping of two variables with using temp variables.

# x = 10
# y = 50

# temp = x
# x = y
# y = temp

# print("Value of x:", x)
# print("Value of y:", y)


# swapping of two variables without using temp variables.


# x = 10
# y = 50

# x, y = y, x

# print("Value of x:", x)
# print("Value of y:", y)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.7 Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

# num = int(input("Enter a Number:")) 
# if num % 2 == 0:
#   print("Given number is Even") 
# else: 
#   print("Given number is Odd")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.8 Write a Python program to test whether a passed letter is a vowel or not.

# c = (input('Enter the charector:'))

# if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
#     print(c, "is a vowel") 
# else:
#     print(c, "is a not a vowel")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Q.9 Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

# a = int(input("Enter the First number  : "))
# b = int(input("Enter the second number : "))
# c = int(input("Enter the third number  : "))

# if a == b or b == c or c ==a:
#     print("Sum is : ", 0)
    
# else:
#     print("Sum is : ", a+b+c)    
 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q.10 Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

# a = int(input("enter a "))
# b = int(input("enter b "))

# if a == b or a-b == 5 or b-a == 5 or a+b == 5:
#   print("True")

# else:
#   print("False")

