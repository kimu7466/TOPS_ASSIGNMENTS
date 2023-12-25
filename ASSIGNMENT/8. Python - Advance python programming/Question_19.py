# 19. How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.


try:
    a=int(input("Enter Numvber1: "))
    b=int(input("Enter Numvber2: "))
    print(a/b)
except ValueError as v:
    print("Integers allowed",v)
except ZeroDivisionError as z:
    print("Not allowed to divide by zero",z)
except:
    print("Unknown Error")
finally:
    print("I am part of finally and I will execute always.")
