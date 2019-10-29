# this program takes input from a user on what constraints they want put in place for their password, and generates a random password to fit those constraints

# imports
import string
import random

# get password length and check to make sure it is valid
while True:
    value = raw_input("How long do you want your password to be (a good password is at least 8 characters long)?\n")
    try:
        password_length = int(value)
    except ValueError:
        print("\nThe password length must be an integer.\n")
        continue
    if password_length < 0:
        print("The password length cannot be less than zero.\n")
        continue
    break
current_length = password_length

# get number of uppercase letters in the password, and check to make sure it is valid
while True:
    value = raw_input("How many uppercase letters do you want your password to have (%s characters remaining)?\n" % current_length)
    try:
        num_uppercase = int(value)
    except ValueError:
        print("\nThe number of uppercase numbers must be an integer.\n")
        continue
    if num_uppercase > current_length or num_uppercase < 0:
        print("The chosen number cannot exceed the number of characters remaining in the password, or be less than zero.\n")
        continue
    break
current_length -= num_uppercase

# get number of numbers in the password, and check to make sure it is valid
while True:
    value = raw_input("How many numbers do you want your password to have (%s characters remaining)?\n" % current_length)
    try:
        num_numbers = int(value)
    except ValueError:
        print("\nThe number of numbers must be an integer.\n")
        continue
    if num_numbers > current_length or num_numbers < 0:
        print("The chosen number cannot exceed the number of characters remaining in the password, or be less than zero.\n")
        continue
    break
current_length -= num_numbers

# get number of symbols in the password, and check to make sure it is valid
while True:
    value = raw_input("How many symbols do you want your password to have (%s characters remaining)?\n" % current_length)
    try:
        num_symbols = int(value)
    except ValueError:
        print("\nThe number of numbers must be an integer.\n")
        continue
    if num_symbols > current_length or num_symbols < 0:
        print("The chosen number cannot exceed the number of characters remaining in the password, or be less than zero.\n")
        continue
    break
current_length -= num_symbols


# create password
password = ''.join([random.choice(string.ascii_uppercase) for n in xrange(num_uppercase)] #  add uppercase letters
                   + [random.choice(string.digits) for n in xrange(num_numbers)] #  add numbers
                   + [random.choice(string.punctuation) for n in xrange(num_symbols)] #  add symbols
                   + [random.choice(string.ascii_lowercase) for n in xrange(current_length)]) #  add lowercase letters

# randomize characters in password
new_pass = ''.join(random.sample(password, len(password)))

# print password
print(new_pass)
