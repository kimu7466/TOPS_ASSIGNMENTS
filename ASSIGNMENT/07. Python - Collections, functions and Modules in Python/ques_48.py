# Q.48 Write a Python function to check whether a number is in a given range.

def count(list1, s, e):
	return len(list(filter(lambda x: s <= x <= e, list1)))

list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70]
s = 20
e = 40
print(count(list1, s, e))

# output Will be 5 
