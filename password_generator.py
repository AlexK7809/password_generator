""" Generates random passwords"""
import random
import string
letters = string.ascii_letters
banner_message = '* AWESOME Password Generator PROGRAM *'

stars = '*' * len(banner_message)
print(stars)
print(banner_message)
print(stars)
while True:
    try:
        password_length = int(input('Enter Password Length: '))
        break
    except ValueError:
        print('Error: Enter an integer number. Try again')
password = ''
for letter in range(password_length):
    random_letter = random.choice(letters)
    password = password + random_letter
print('Your password is: ' + password)