#------------------------------------------------#
#    Author: Manoj Selvin                        #
#    Description: Encrypts and decrypts strings  #
#------------------------------------------------#

#encrypts strings
def encrypt(text):
    encrypted_string = ''
    for char in text:
        encrypted_string += chr(ord(char) + 3)
        
    return encrypted_string
    
#decrypts strings
def decrypt(text):
    decrypted_string = ''
    for char in text:
        decrypted_string += chr(ord(char) - 3)
        
    return decrypted_string    


#taking inputs
data = input()

#actual data
print("Actual data: " + data)

#encrypted text
encrypted_data = encrypt(data)
print("Encrypted data: " + encrypted_data)

#decrypted text
decrypted_data = decrypt(encrypted_data)
print("Decrypted data: " + decrypted_data)

