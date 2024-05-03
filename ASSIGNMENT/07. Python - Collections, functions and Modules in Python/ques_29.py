# Q.29  Write a Python program to unzip a list of tuples into individual lists. 

tuple = [('123'),('ABC'), ('456')]

print(list(zip(*tuple)))
