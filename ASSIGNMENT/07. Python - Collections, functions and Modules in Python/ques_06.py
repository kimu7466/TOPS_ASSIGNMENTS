
# Q.6 Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same  from a given list of strings.  

list=["madem","3643","apple","3753"]
ch = 0
for list in list:
	if len(list) > 1 and list[0] == list[-1]:
	  ch += 1
print(ch)


