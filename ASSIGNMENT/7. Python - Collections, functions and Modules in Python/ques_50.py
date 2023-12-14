# Q.50  Write a Python function that checks whether a passed string is palindrome or not.

def palindrom(string):
       reversestring=''.join(reversed(string))
       if string == reversestring:
              return 'The string is palindrom.'
       return 'Thre string is not palindrom.'

print(palindrom(input('Enter a string: ')))
