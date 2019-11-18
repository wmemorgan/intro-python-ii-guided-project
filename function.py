# define a doubling function that passes args by value
def double_num(x):
    x = x * 2 

print(double_num(5))

# # define a doubling function that passes args by reference
# # define a double function, that doubles every item in a list
def double_list(li):
    for i in range(0, len(li)):
        li[i] = li[i] * 2 #the list is passed by reference, thus changing it here changes the original list

# # try out our functions
new_list = [1, 2, 3, 4]

print(new_list) 
double_list(new_list) #notice how the function does not return a new list, it just modifies the list thats passed in
print(new_list)

# redefining a argument no longer keeps the reference to the original list
def redefine_reference_argument(li):
    li = [0 , 1] # here we redefine the list
    print(li) # its still [0, 1] here

list_2 = [ 0 ]
print(list_2) 
redefine_reference_argument(list_2)
print(list_2) # the list never changes to [0, 1]


# Arguments
# write a function print_three_numbers that prints all numbers in the order they are given
def print_three_numbers(number1, number2, number3):
    print(f'number1 is: {number1}')
    print(f'number2 is: {number2}')
    print(f'number3 is: {number3}')

## call it with positional arguments
print_three_numbers(5, 2, 3)

# call it with named arguments
print_three_numbers(number1=5, number2=2, number3=3)

# call it with positional and named arguments
print_three_numbers(5, number3=3, number2=2)

## write a function called print_all_numbers that will print any amount of numbers
def print_all_numbers(*numbers):
    for i in range(len(numbers)):
        print(f'num at {i} is {numbers[i]}')

# print_all_numbers(1)
# print_all_numbers(1,2,3,4,5)
# print_all_numbers(10, 111, 11111, 111,1)

## write a function that will print all numbers, in reverse order if we specify a reverse variable
def print_all_numbers_maybe_reverse(*numbers, reverse=True):
    if reverse:
        numbers = numbers[::-1]
    for i in range(len(numbers)):
        print(f'num at {i} is {numbers[i]}')

print_all_numbers_maybe_reverse(1)
print_all_numbers_maybe_reverse(1,2,3)
print_all_numbers_maybe_reverse(1,2,3,4)
