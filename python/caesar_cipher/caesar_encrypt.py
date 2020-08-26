import string
alphabet = string.ascii_lowercase


def encrypt(text,shift):
    '''
    INPUT: text as a string and an integer for the shift value.
    OUTPUT: The shifted text after being run through the Caeser cipher.
    '''

    # Create a normal plain alphabet
    alphabet_list_orig = list(alphabet)
    replaced_list = list(alphabet)
    alphabet_list_shifted = list(alphabet)

    # shift
    temp = 0

    for x in range(0,shift):
        temp = alphabet_list_shifted.pop(0)
        alphabet_list_shifted.append(temp)

    # Convert the string to a list of characters

    char_list = list(text.lower())

    # Find the length of the list
    length_of_input = len(char_list)

    char_index = -1

    for y in char_list:

        char_index = char_index +1
        #print("Char index is {}\n".format(char_index))

        if y in ['?','.','!', ' ']:
            continue

        index = alphabet_list_orig.index(y)

        char_list[char_index] = alphabet_list_shifted[index]


    return_string = "".join(char_list)
    return return_string

message_to_encrypt = "ill be there at three"
encrypted_message = encrypt(message_to_encrypt, 13)
print("The encrypted message is: {}".format(encrypted_message))
