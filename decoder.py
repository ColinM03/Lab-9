# Colin McEliece

def decode(encrypted_message):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += str(int(char) - 3)
    return decrypted_message

