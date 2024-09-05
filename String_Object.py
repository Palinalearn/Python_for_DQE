# Task 1
str_default = """homEwork:
 tHis iz your homeWork, copy these Text to variable.



 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# declaring variables
new_sentence_list = []
sentence_list = []
final_list = []
sentence_delimeter = '\n'
new_line_delimeter = ' '

#  split text to the words
str_word = str_default.split()

# for each word find the LAST WoRDS of each existING SENtence
for item in str_word:
    # change it for lowercase
    item = item.lower()
    # find the mistake 'iz'
    if item == 'iz':
        # change it to 'is'
        item = 'is'
    # for each last word
    if item.endswith('.'):
        # create new sentence
        new_sentence_list.append(item[0:-1])
        new_sentence = new_line_delimeter.join(new_sentence_list).capitalize()
    # collect all sentence into one text
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

# insert new sentence after needed one
final_list.insert(3, new_sentence)
# add create final text
final_text = sentence_delimeter.join(final_list)

# print final text
print(final_text)

# declaring variables
i = 0

# calculate nuMber OF Whitespace characteRS
for element in str_default:
    for item in element:
        if item.isspace():
            i = i + 1

print(i)