# Q.9 Write a Python function that takes two lists and returns true if they have at least one common member.

list1=[1,2,3,4,5]
list2=[5,6,7,8,9]
result = False
for x in list1:
 for y in list2:
	 if x == y:
		 result = True
print(result)
if result:
    print("Lists have at least one common member")
else:
    print("Lists do not have any common member")
