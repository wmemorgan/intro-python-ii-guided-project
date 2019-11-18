# define a doubling function that passes args by value
def add_letter(x):
  x = x + 'l'
  
new_str = 'abc'
print(new_str)
print(add_letter(new_str))
print(new_str)

"""
Items that are passed by reference:
- Lists (arrays)
- Dictionaries (objects)
- Tuples???
"""

# define a doubling function that passes args by reference
# define a double function, that doubles every item in a list
def double_list(li):
  for i in range(0, len(li)):
    li[i] *= 2

# try out our functions
# new_list = [1, 2, 3, 4]
# print(new_list)
# double_list(new_list)
# print(new_list)

# list_2 = [0]
# def the_ugly_truth(li):
#   li.append(1)
#   print(li)

# print(list_2)
# the_ugly_truth(list_2)
# print(list_2)
# SAFETY TIP: Don't reassign your arguments inside your functions

# Ar