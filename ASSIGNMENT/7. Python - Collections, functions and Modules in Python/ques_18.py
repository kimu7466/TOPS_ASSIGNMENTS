# Q.18 What is tuple? Difference between list and tuple. 

'''
# TUPLE
#tuple is a collection of elements of similar or different datatype
# tuple is immutable------no changes are allowed
# tuple is ordered--------every elements in list has its own index number
# tuple is defined in () brackets
# tuple allows duplicates values because they all have different index numbers
'''

'''
DIFFRENCE BETWEEN LIST AND TUPLE---

1. Mutability:
   - List: Lists are mutable, which means you can change, add, or remove elements after creating the list. You can use methods like append(), 
     extend(), insert(), and remove() to modify a list.
   - Tuple: Tuples are immutable, meaning once you create a tuple, you cannot change its content. You cannot add or remove elements from a tuple.
     This immutability can be useful in cases where you want to ensure that the data remains constant.

2. Syntax:
   - List: Lists are created using square brackets, for example, my_list = [1, 2, 3].
   - Tuple: Tuples are created using parentheses, for example, my_tuple = (1, 2, 3). You can also create a tuple without parentheses, e.g.,
     my_tuple = 1, 2, 3.

3. Performance:
   - Lists, being mutable, can be less memory-efficient and slower in certain operations compared to tuples.
   - Tuples, being immutable, are generally more memory-efficient and faster for simple operations, making them a better choice when you need to 
     store data that should not change.

4. Use Cases:
   - Lists are often used for collections of items where you may need to add, remove, or modify elements during the program's execution.
   - Tuples are typically used when you want to ensure that the data remains constant and should not be changed, such as representing coordinates,
     dates, or configurations.

5. Iteration:
   - Both lists and tuples can be iterated using loops like `for` or by using list comprehensions. Iterating through a tuple can be slightly faster
     due to its immutability.

'''
