import random
import string

# Task 1:create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

print('')
print('Task 1')


# define a random number of dictionaries
def create_random_number_of_dicts(a):
    dicts_count = a
    # start with the first dict
    dict_number = 1
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
        # add dict into the list
        dicts_list.append(new_dict)
        # add iteration and continue work with other dict
        dict_number = dict_number + 1
    return dicts_list


print('')
# print the result
print(f'Final result {create_random_number_of_dicts(6)}')

# Task 2: get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

print('')
print('Task 2')


# declaring variables
# empty dict for common dict without numbering
def common_dict(dicts_list):
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
    return final_dict


# print the final result
print(common_dict(create_random_number_of_dicts(3)))

# Tasks for STRINGS
# Task 3:
print('')
print('Task 3')

str_default = """homEwork:
 tHis iz your homeWork, copy these Text to variable.



 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


#  split text to the words
def split_text_to_the_words(default_string):
    str_word = default_string.split()
    return str_word


#  Change case of all words
def change_case(word_list):
    new_list = []
    # for each word find the LAST WoRDS of each existING SENtence
    for item in word_list:
        # change it for lowercase
        new_list.append(item.lower())
    return new_list


#  fix mistake
def fix_mistake(mistake, fix, word_list):
    new_list = []
    for item in word_list:
        # find the mistake 'iz'
        if item == mistake:
            # change it to 'is'
            new_list.append(fix)
        else:
            new_list.append(item)
        # for each last word
    return new_list


#  create new sentence
def create_new_sentences(word_list):
    new_sentence_list = []
    new_line_delimeter = ' '
    for item in word_list:
        if item.endswith('.'):
            # create new sentence
            new_sentence_list.append(item[0:-1])
            new_sentence = new_line_delimeter.join(new_sentence_list).capitalize()
    new_sentence = new_sentence + '.'
    return new_sentence


def collect_all_sentences(word_list):
    # collect all sentence into one text
    sentence_list = []
    final_list = []
    new_line_delimeter = ' '
    for item in word_list:
        if not item.endswith('.'):
            # each word except word with point add into list
            sentence_list.append(item)
        else:
            # then add word with point
            sentence_list.append(item)
            # create sentence
            sentence = new_line_delimeter.join(sentence_list).capitalize()
            #  add sentence into the new list
            final_list.append(sentence)
            # clear sentence list
            sentence_list = []
    return final_list


def insert_new_sentence(position, sentence_list, sentence):
    return sentence_list.insert(position, sentence)


def change_all_text(default_string, new_sentence_position, mistake, fix, sentence_delimeter):
    #  split text to the words
    str_word = split_text_to_the_words(default_string)
    #  Change case of all words
    word_list = change_case(str_word)
    #  fix mistake
    word_list = fix_mistake('iz', 'is', word_list)
    # create new sentence
    new_sentence = create_new_sentences(word_list)
    # create final list
    final_list = collect_all_sentences(word_list)
    # add new sentence into list
    insert_new_sentence(3, final_list, new_sentence)
    # create final text
    final_text = sentence_delimeter.join(final_list)
    return final_text


print(change_all_text(str_default, 3, 'iz', 'is', '\n'))


# calculate nuMber OF Whitespace characteRS
def calculate_whitespace(default_string):
    i = 0
    for element in default_string:
        for item in element:
            if item.isspace():
                i = i + 1
    return i


print(calculate_whitespace(str_default))
