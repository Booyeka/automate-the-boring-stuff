








#take list of strings and convert it to one single string value.  strings sepereated by "," and insert the word "and" in between the last and second to last string in list




# FUNCTION - creating a string of inputed list of strings
def to_string(list):

    string = ''

    # LOOP by numerical index of inputed list
    for i in range(len(list)):

        # CONDITIONAL - if last index, add to string and break
        if i == len(list)-1:
            string += list[i]
            break

        # adding current index of list to string value, seperated by a comma
        string += list[i] +', '

        # CONDITIONAL - second to last index add "and "
        if i == len(list)-2:
            string += 'and '

    print(string)
    return string
    


#test list
spam = ['apples', 'bananas', 'tofu', 'cats']

#list to store manually inputed strings
list_of_strings = [] 


# LOOP
while True:
     # prompt to enter strings
    print('enter words, enter nothing to end')
    entered_string = input() 

    # CONDITIONAL
    # an empty string will break the loop
    if entered_string == '':
        break

    # adding entered string to list
    list_of_strings.append(entered_string)


# function call with list of inputed strings
to_string(list_of_strings)



