# 8. Write a python program to find the longest words.

def longest_word(file_name):

  with open('file_name.txt', 'r') as infile:
      words = infile.read().split()
      
  max_len = len(max(words, key = len))
  return [word for word in words if len(word) == max_len]

print(longest_word('file_name.txt'))  