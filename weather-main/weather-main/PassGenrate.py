import random
import string

def generate_password(length=12):
    # Define character sets for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password (default is 12): "))
    password = generate_password(length)
    print("Generated Password:", password)

if _name_ == "_main_":
    main()
