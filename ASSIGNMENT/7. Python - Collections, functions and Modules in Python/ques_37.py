# Q.37 Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 

dict = {}

for num in range(1, 16):
    dict[num] = num ** 2

print("Dictionary with squares of keys:")
print(dict)
