# Q.61 Write a Python program to returns sum of all divisors of a number 

# import math

# def sum_of_divisors(number):
#     divisor_sum = 0

#     for i in range(1, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             divisor_sum += i

#             if i != number // i:
#                 divisor_sum += number // i

#     return divisor_sum

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

num = int(input("Enter a number: "))

result = get_divisors(num)
print(f"The divisors of {num} are: {result}")
