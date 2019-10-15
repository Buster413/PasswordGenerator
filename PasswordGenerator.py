import string
import random

# this program takes input from a user on what constraints they want put in place for their password, and generates a random password to fit those constraints

# get password contstraints from user
password_length = input("How long do you want your password to be (a good password is at least 8 characters long)?\n")
num_uppercase = input("How many uppercase letters do you want your password to have?\n")
num_numbers = input("How many numbers do you want your password to have?\n")
num_symbols = input("How many symbols do you want your password to have?\n")

# create password
password = ''.join([random.choice(string.ascii_uppercase) for n in xrange(num_uppercase)] #  add uppercase letters
                   + [random.choice(string.digits) for n in xrange(num_numbers)] #  add numbers
                   + [random.choice(string.punctuation) for n in xrange(num_symbols)] #  add symbols
                   + [random.choice(string.ascii_lowercase) for n in xrange(password_length - num_uppercase)]) #  add lowercase letters

# randomize characters in password
new_pass = ''.join(random.sample(password, len(password)))

# print password
print(new_pass)