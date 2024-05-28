
# Q.62 Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

def find_max_min(numbers):
    if not numbers:
        return None, None  

    max_num = numbers[0]  
    min_num = numbers[0]  

    for num in numbers:
        if num > max_num:
            max_num = num  
        elif num < min_num:
            min_num = num  

    return max_num, min_num

decimal_numbers = [3.14, 2.71, 5.5, 1.618, 0.707]
maximum, minimum = find_max_min(decimal_numbers)
print(f"The maximum number is: {maximum}")
print(f"The minimum number is: {minimum}")

