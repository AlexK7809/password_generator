""" Generates random passwords"""
import random
import string
letters = string.ascii_letters

password_length = int(input('Ennter Password Length: '))
password = ''
for letter in range(password_length):
    random_letter = random.choice(letters)
    password = password + random_letter
print('Your password is: ' + password)