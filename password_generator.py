""" Generates random passwords"""
import random
import string
letters = string.ascii_letters
banner_message = '* AWESOME Password Generator PROGRAM *'

stars = '*' * len(banner_message)
print(stars)
print(banner_message)
print(stars)

password_length = int(input('Enter Password Length: '))
password = ''
for letter in range(password_length):
    random_letter = random.choice(letters)
    password = password + random_letter
print('Your password is: ' + password)