#Elijah Holbrook

def encode(decrypted_message):
    encrypted_message = ""
    for char in decrypted_message:
        encrypted_message += str(int(char) + 3)
    return encrypted_message
