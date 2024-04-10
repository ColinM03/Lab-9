# Colin McEliece
from decoder import *
from encoder import *
def main():
    while True:
        print("Menu")
        print("------------- ")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit \n")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            message = input("Please enter your password to encode: ")
            encoded_message = encode(message)
            print("Your password has been encoded and stored! \n")
        elif choice == 2:
            print(f"The encoded password is {encoded_message}, and the original password is {decode(encoded_message)}. \n")
        elif choice == 3:
            break
        else:
            print("Invalid input. \n")

if __name__ == "__main__":
    main()