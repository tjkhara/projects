def decrypt(text,shift):
    '''
    INPUT: A shifted message and the integer shift value
    OUTPUT: The plain text original message.
    '''

    # Create a normal plain alphabet
    import string
    alphabet = string.ascii_lowercase

    # Create a normal plain alphabet
    alphabet_list_orig = list(alphabet)
    replaced_list = list(alphabet)
    alphabet_list_shifted = list(alphabet)

    # Create a shifted version of this alphabet with the shift value.
    temp = 0

    for x in range(0,shift):
        temp = alphabet_list_shifted.pop(0)
        alphabet_list_shifted.append(temp)

    # Create a list from the characters of text and convert each character to lower case
    char_list = list(text.lower())

    length_of_input = len(char_list)

    char_index = -1

    for y in char_list:

        char_index = char_index +1

        if y in ['?','.','!', ' ']:
            continue

        index = alphabet_list_shifted.index(y)

        # Take the character from the new list at this index and replace it in the list
        char_list[char_index] = alphabet_list_orig[index]

    return_string = "".join(char_list)
    return return_string

message_to_decrypt = 'vyy or gurer ng guerr'
decrypted_message = decrypt(message_to_decrypt,13)
print(decrypted_message)


