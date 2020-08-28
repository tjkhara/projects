# as a command line argument enter the string that needs to be encrypted

from cryptography.fernet import Fernet
import sys

print("The name of this python script is: ", sys.argv[0])
print("The string entered for encryption is: ", sys.argv[1])

# generate a key

key = Fernet.generate_key()
print("The key is: {}".format(key))
print("Please store this key in a safe place as you will need it to decrypt your data")

# generate cipher

cipher = Fernet(key)

# text to encrypt needs to be entered here

input_text = sys.argv[1]
binary_input_text = input_text.encode()

encrypted_message = cipher.encrypt(binary_input_text)

print("The encrypted text is: ")
print(encrypted_message)
