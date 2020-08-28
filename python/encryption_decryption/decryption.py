from cryptography.fernet import Fernet
import sys

# first command line argument is the string to be decrypted not in binary 
# second argument is the key in not in binary

print("The string to be decrypted is: {}".format(sys.argv[1]))

decryption_string = sys.argv[1].encode()

key = sys.argv[2].encode()

print("The key in binary is: {}".format(key))

# decryption

other_cipher = Fernet(key)
decrypted_message = (other_cipher.decrypt(decryption_string)).decode()
print("The decrypted message is: {}".format(decrypted_message))
