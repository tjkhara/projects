# Caesar cipher encryption, decryption, and brute force method to decrypt

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


def brute_force(message):
    """
    INPUT: A shifted message
    OUTPUT: Prints out every possible shifted message.
            One of the printed outputs should be readable.
    """

    # Use your previous decrypt() method and call it for every possible shift
    # using a For Loop.

    for x in range(1,27):
        print("Using shift value of {}".format(x))
        print(decrypt(message, x))
        print ("\n")


print("This is the encrypted message: \n")
encrypted_message = encrypt("Hi the attack will be at three am", 13)
print(encrypted_message)
print("\n")

print("This is the decrypted message: \n")
decrypted_message = decrypt(encrypted_message, 13)
print(decrypted_message)
print("\n")


print("Using brute force to crack the encryption: \n")
brute_force(encrypted_message)
