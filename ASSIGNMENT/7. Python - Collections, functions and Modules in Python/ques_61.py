# Q.61 Write a Python program to returns sum of all divisors of a number 

# import math

# def sum_of_divisors(number):
#     # Initialize the sum
#     divisor_sum = 0

#     # Iterate up to the square root of the number
#     for i in range(1, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             # If 'i' is a divisor, add it to the sum
#             divisor_sum += i

#             # If the divisor is not the square root of the number, add its pair
#             if i != number // i:
#                 divisor_sum += number // i

#     return divisor_sum

# # Taking user input for the number
# num = int(input("Enter a number: "))

# result = sum_of_divisors(num)
# print(f"The sum of all divisors of {num} is: {result}")

# ###########
def get_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

# Taking user input for the number
num = int(input("Enter a number: "))

result = get_divisors(num)
print(f"The divisors of {num} are: {result}")
