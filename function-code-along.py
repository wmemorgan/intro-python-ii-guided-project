# define a doubling function that passes args by value
"""
def add_letter(x):
  x = x + 'l'
"""
# new_str = 'abc'
# print(new_str)
# print(add_letter(new_str))
# print(new_str)

"""
Items that are passed by reference:
- Lists (arrays)
- Dictionaries (objects)
- Tuples???
"""

# define a doubling function that passes args by reference
# define a double function, that doubles every item in a list
# def double_list(li):
#   for i in range(0, len(li)):
#     li[i] *= 2

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

# Arguments
# write a function print_three_numbers that prints all numbers in the order they are given
def print_three_numbers(number1, number2, number3):
  print(f'number1: {number1}')
  print(f'number2: {number2}')
  print(f'number3: {number3}')

## call it with positional arguments
# print_three_numbers(5, 2, 3)

# call it with named arguments
# print_three_numbers(number1=1, number2=2, number3=3)


# call it with positional and named arguments
print_three_numbers(5, number2=2, number3=3)

## write a function called print_all_numbers that will print any amount of numbers
def print_all_numbers(*args):
  for i in range(len(args)):
    print(f'num at {i} is {args[i]}')

# print_all_numbers(1)
# print_all_numbers(1, 2, 3, 4, 5)
# print_all_numbers(10, 111, 11111, 111, 1)

## write a function that will print all numbers, in reverse order if we specify a reverse variable
def print_all_numbers_maybe_reverse(*args, reverse=False):
  if reverse:
    args = args[::-1]
  for i in range(len(args)):
    print(f'num at {i} is {args[i]}')

print_all_numbers_maybe_reverse(1)
print_all_numbers_maybe_reverse(1, 2, 3)
print_all_numbers_maybe_reverse(1, 2, 3, 4, reverse=True)
