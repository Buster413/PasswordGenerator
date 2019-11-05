# this program takes input from a user on what constraints they want put in place for their password, and generates a random password to fit those constraints

# imports
import string
import random


# get requirements from user and generate password
def generate_password():
    # get password length and check to make sure it is valid
    while True:
        try:
            password_length = int(input("How long do you want your password to be? A good password is at least 9 characters long.\n"))
        except ValueError:
            print("\nThe password length must be an integer.\n")
            continue
        if password_length < 0:
            print("The password length cannot be less than zero.\n")
            continue
        if password_length == 0:
            print("Chosen password length is 0, exiting program.")
            exit(0)
        break
    current_length = password_length

    # get number of uppercase letters in the password, and check to make sure it is valid
    if current_length != 0:
        while True:
            value = input("How many uppercase letters do you want your password to have (%s characters remaining)?\n" % current_length)
            try:
                num_uppercase = int(value)
            except ValueError:
                print("\nThe number of uppercase numbers must be an integer.\n")
                continue
            if num_uppercase > current_length or num_uppercase < 0:
                print("The chosen number cannot exceed the number of characters remaining in the password, or be less than zero.\n")
                continue
            current_length -= num_uppercase
            break
    else:
        num_uppercase = 0
        num_numbers = 0
        num_symbols = 0

    # get number of numbers in the password, and check to make sure it is valid
    if current_length != 0:
        while True:
            value = input("How many numbers do you want your password to have (%s characters remaining)?\n" % current_length)
            try:
                num_numbers = int(value)
            except ValueError:
                print("\nThe number of numbers must be an integer.\n")
                continue
            if num_numbers > current_length or num_numbers < 0:
                print("The chosen number cannot exceed the number of characters remaining in the password, or be less than zero.\n")
                continue
            current_length -= num_numbers
            break
    else:
        num_numbers = 0
        num_symbols = 0

    # get number of symbols in the password, and check to make sure it is valid
    if current_length != 0:
        while True:
            value = input("How many symbols do you want your password to have (%s characters remaining)?\n" % current_length)
            try:
                num_symbols = int(value)
            except ValueError:
                print("\nThe number of numbers must be an integer.\n")
                continue
            if num_symbols > current_length or num_symbols < 0:
                print("The chosen number cannot exceed the number of characters remaining in the password, or be less than zero.\n")
                continue
            current_length -= num_symbols
            break
    else:
        num_symbols = 0

    # create password
    password = ''.join([random.choice(string.ascii_uppercase) for n in range(num_uppercase)]  # add uppercase letters
                       + [random.choice(string.digits) for n in range(num_numbers)]  # add numbers
                       + [random.choice(string.punctuation) for n in range(num_symbols)]  # add symbols
                       + [random.choice(string.ascii_lowercase) for n in range(current_length)])  # add lowercase letters

    # randomize characters in password
    new_pass = ''.join(random.sample(password, len(password)))

    # print password
    return new_pass


# main method
def main():
    print("Your password is: ", generate_password())

if __name__ == "__main__":
    main()