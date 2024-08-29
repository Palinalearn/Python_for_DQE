import random

# Task 1
# create list of 100 random numbers from 0 to 1000
i = 1
# the empty list
random_list = []

# while loop for creating list with 100 random numbers
# only 100 iteration
while i < 101:
    # random number from 0 to 1000
    random_number = random.randint(0, 1001)
    # add random number into the list
    random_list.append(random_number)
    # add plus one after each iteration
    i = i + 1

# check the result
print('Task 1')
print('the count of random number:', len(random_list))

# Task 2
# sort list from min to max (without using sort())
# empty list for the future sorted list
sorted_list = []

# using sorted() for compare it with our result
print('Task 2')
print(sorted(random_list))

# while loop for all list's element
while random_list:
    # everytime take the first element
    checked_number = random_list[0]
    # and remove it from the random_list
    random_list.pop(0)
    # if it is the first element in our new sorted_list we just add checked_number
    if len(sorted_list) == 0:
        # add first element
        sorted_list.append(checked_number)
    # if sorted_list is not empty try to find element in sorted_list list which is more then checked_number
    else:
        #  sorted_list element index
        i = 0
        # compare element from sorted_list with checked_number
        while i in range(0, len(sorted_list)) and checked_number > sorted_list[i]:
            #  add 1 for iteration and index
            i = i + 1
        # add checked_number instead of found element or into the end
        sorted_list.insert(i, checked_number)

# compare results
print(sorted_list)

# Task 3
# calculate average for even and odd numbers
# declaring variables
sum_even = 0
i_even = 0
sum_odd = 0
i_odd = 0

# for each element from our list
for x in sorted_list:
    # Check that it is even number or odd
    if x in range(0, 1001, 2):
        # find a sum
        sum_even = sum_even + x
        # add count
        i_even = i_even + 1
    # Check that it is even number or odd
    if x in range(1, 1001, 2):
        # find a sum
        sum_odd = sum_odd + x
        # add count
        i_odd = i_odd + 1

# Check that we will not delete by zero and if we have 0 even number the everage is equal to 0
if i_even == 0:
    average_even = 0
else:
    average_even = sum_even / i_even

# Check that we will not delete by zero and if we have 0 odd number the everage is equal to 0
if i_odd == 0:
    average_odd = 0
else:
    average_odd = sum_odd / i_odd

print('Task 3')
print('average for even numbers: ', average_even)
print('average for odd numbers: ', average_odd)