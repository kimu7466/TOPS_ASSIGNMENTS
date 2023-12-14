# Q.28 Write a Python program to remove an empty tuple(s) from a list of tuples.

tuplelist = (35,45.87,True," ",[ ],(32,66),{1,2},{ })

tuplelist = [t for t in tuplelist if t]

print(tuplelist)
