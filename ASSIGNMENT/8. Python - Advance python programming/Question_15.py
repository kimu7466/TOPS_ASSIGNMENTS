# 15. When will the else part of try-except-else be executed?

''' The else part is executed when no exception occurs. '''



print("start")
try:
    a = int(input("Enter something: "))
except ValueError:
    print("Please enter only digit")
except NameError:
    print("Please define variable a")
except Exception as e:
    print(f"ERROR : {e}")
else:
    print(a  + 10)

print("end")