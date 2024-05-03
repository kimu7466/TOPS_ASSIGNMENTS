# Q.26  Write a Python program to replace last value of tuples in a list

tuplelist = (1,2,3,4,5,6,7,8,9,10)
tuplelist = list(tuplelist)

tuplelist[9] = 20
tuplelist = tuple(tuplelist)

print(tuplelist)