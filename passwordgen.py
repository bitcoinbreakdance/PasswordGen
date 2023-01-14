import random
import string
import pyfiglet

def generate_password():
    """Generates a new complex 9-digit password"""
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=9))
    return password

def save_password(password):
    """Saves the given password to a text file named 'password_gen.txt'"""
    with open("password_gen.txt", "a") as file:
        file.write(password + "\n")

def main():
    """Displays a menu with a banner and handles user input"""
    ascii_banner = pyfiglet.figlet_format("Password Gen", font = "big") # using 'big' font
    print("\033[1;34;40m" + ascii_banner.center(80, " ") + "\033[0;37;40m")
    print("\033[1;32;40m" + "1. Generate Password".center(80, " ") + "\033[0;37;40m")
    option = input("Select an option: ")
    if option == "1":
        password = generate_password()
        print("New password: ", password)
        save_password(password)
        print("Password saved to password_gen.txt")
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()