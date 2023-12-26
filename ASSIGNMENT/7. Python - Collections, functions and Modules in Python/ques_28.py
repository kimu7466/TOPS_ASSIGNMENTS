# Q.28 Write a Python program to remove an empty tuple(s) from a list of tuples.

tuplelist = (35,45.87,True,'',[ ],(32,66),{1,2},{ })

tuplelist = [ imroz for imroz in tuplelist if imroz]

print(tuplelist)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#2.



# def remove_empty_tuples(tuple_list):
#     # Use list comprehension to filter out empty tuples
#     non_empty_tuples = [tup for tup in tuple_list if tup]
#     return non_empty_tuples

# # Example list of tuples including empty tuples
# list_of_tuples = [(1, 2), (), (3,), (4, 5), (), (), (6,), (), ((),), (7, 8, 9), ()]

# # Remove empty tuples from the list
# result = remove_empty_tuples(list_of_tuples)

# # Display the result after removing empty tuples
# print("List after removing empty tuples:", result)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#3.

# def remove_empty_tuples(tuple_list):
#     non_empty_tuples = []
#     for tup in tuple_list:
#         if tup:  # Check if the tuple is not empty (truthy)
#             non_empty_tuples.append(tup)
#     return non_empty_tuples

# # list_of_tuples = [(1, 2), (2), (3,), (4, 5), (), (), (6,), (), ((),), (()), (7, 8, 9), ()]

# list_of_tuples = [(1, 2), (2), (3,), ["imroz","KHan",'PATHAN'], [], {"name":'imroz',"age":"25"}, (4, 5), (), (), (6,), (), (7, 8, 9), (), {()},({}), ((),), (())]

# # Remove empty tuples from the list
# result = remove_empty_tuples(list_of_tuples)

# # Display the result after removing empty tuples
# print("List after removing empty tuples:", result)



# tuple = ( 1 ,{}, (),(57),{11},[54],"ab",""  )

# filtered_tuple = [(str(t)+"_imroz_") for (t) in tuple if t=="ab" ]

# print(filtered_tuple)