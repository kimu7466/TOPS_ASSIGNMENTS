# Q.2 How will you remove last object from a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]? 

# One way is to use the pop() method. This method removes the last element of a list by default,
# or you can specify the index of the element you want to remove.
  
  #EXAMPLE 
  
list1 = [2, 33, 222, 14, 25]

list1.pop()
print(list1)
# [2, 33, 222, 14]


print(list1[-1])
# 14
            
