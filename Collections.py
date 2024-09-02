import random
import string

# Task 1:create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

print('')
print('Task 1')
# define a random number of dictionaries
dicts_count = random.randint(2, 10)
# stert with the first dict
dict_number = 1
print('Dicts count: ', dicts_count)
# the empty list for our dicts
dicts_list = []

# For each dicts generate keys and values
while dict_number <= dicts_count:
    # define number of items
    # english alfabet has only 26 values and they can't repeat on our dict
    items_count = random.randint(1, 26)
    # start from the first one item from our dict
    i = 1
    # create new dict
    new_dict = {}
    # and for each elements (the number of elements is equal to items_count variable)
    while i <= items_count:
        # we create key
        dict_key = random.choice(string.ascii_lowercase)
        # if key is already exist we try to generate a new one
        while dict_key in new_dict.keys():
            # create a key one mote time
            dict_key = random.choice(string.ascii_lowercase)
        # generate value for our dict
        dict_value = random.randint(0, 100)
        # add new item into the new_dict
        new_dict[dict_key] = dict_value
        # add iteration for each element
        i = i + 1
    # print each dict
    print(f'DICT {dict_number}: {new_dict}')
    # add dict into the list
    dicts_list.append(new_dict)
    # add iteration and continue work with other dict
    dict_number = dict_number + 1

print('')
# print the result
print(f'Final result {dicts_list}')

# Task 2: get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

print('')
print('Task 2')
# declaring variables
# empty dict for common dict without numbering
common_dict = {}
# empty dict for for storing data about old dicts
dict_for_numbering = {}
# empty dict for final result
final_dict = {}
i = 1

# work eith each dict
for item in dicts_list:
    # for each element in dict
    for key, value in item.items():
        #  check if this key exists in our new common dict
        if key not in common_dict.keys():
            # if not create a new element
            common_dict[key] = value
            # and save dict number and flag that this key we met firstly
            dict_for_numbering[key] = [i, True]
        # if key exist check the value, if value is more that existing one, change it
        elif key in common_dict.keys() and value >= common_dict[key]:
            # change the value
            common_dict[key] = value
            # add new dict value and new flag
            dict_for_numbering[key] = [i, False]
        else:
            # if value is less then existing one change only flag
            dict_for_numbering[key][1] = False
    #  iteration plus 1 for dict number
    i = i + 1

# create new dict with all condition
for key, value in common_dict.items():
    # if we meet the key more than once, then we change it to a new value with a prefix
    if key in dict_for_numbering.keys() and not dict_for_numbering[key][1]:
        # get dict number
        dict_number = str(dict_for_numbering[key][0])
        # variable for a new key
        new_key = key + '_' + dict_number
        # rename key with dict number with max value
        final_dict[new_key] = value
    # if key is only in one dict - take it as is
    else:
        final_dict[key] = value

# print the final result
print(final_dict)






