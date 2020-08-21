import string
alphabet = string.ascii_lowercase
# print(alphabet)
# print(list(alphabet))


def encrypt(text,shift):
    '''
    INPUT: text as a string and an integer for the shift value.
    OUTPUT: The shifted text after being run through the Caeser cipher.
    '''
    
    # Create a normal plain alphabet
    alphabet_list_orig = list(alphabet)
    replaced_list = list(alphabet)
    alphabet_list_shifted = list(alphabet)
    
    #Print the original alphabet list
    #print("The original alphabet list is ")
    #print(list(enumerate(alphabet_list_orig)))
    #print("\n")
    
    # Create a shifted version of this alphabet 
    # (Try slicing using the shift and then reconcatenating the two parts)
    temp = 0
    
    for x in range(0,shift):
        temp = alphabet_list_shifted.pop(0)
        alphabet_list_shifted.append(temp)
        
    #print("Alphabet list shifted is: ")
    #print(list(enumerate(alphabet_list_shifted)))
    #print("\n")
    
    # Use a for loop to go through each character in the original message.
    # Then figure out its index match in the shifted alphabet and replace.
    # It might be helpful to create an output variable to hold the new message.
    
    # Convert the string to a list of characters
    text_list = text.split()
    
    char_list = []
    
    for word in text_list:
        for char in word.lower():
            char_list.append(char)
    
    #print("The char_list is: ")
    #print(char_list)
    #print("\n")
    
    # Find the length of the list
    length_of_input = len(char_list)
    
    char_index = -1
    #length_of_char_list = len(char_list)
    #print("The length of char_list is {}\n".format(length_of_char_list))
    
    for y in char_list:
        
        char_index = char_index +1
        #print("Char index is {}\n".format(char_index))
        
        if y in ['?','.','!']:
            continue
        
        # Replace the first character
        # Find the index of the first character
        index = alphabet_list_orig.index(y)
        #print("The index for replacement is: ")
        #print(index)
        #print("\n")

        # Take the character from the new list at this index and replace it in the list
        char_list[char_index] = alphabet_list_shifted[index] 

        #print("Replaced list is: ")
        #print(char_list)
        #print("\n")
    
    # Print the completed replaced_list
    #print("The completed replaced_list is: ")
    #print(char_list)
    #print("\n")
    
    # Keep in mind you may want to skip punctuation with an if statement.
    # Done
    
    # Return the shifted message. Use ''.join() method
    # Done
    # if you still have it as a list.
    # Done
    return_string = "".join(char_list)
    return return_string
    #pass

encrypted_string = encrypt("Hello how are you?", 2)

print("The encrypted string is {}".format(encrypted_string))
