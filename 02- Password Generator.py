# Password Generator

import string
import random

print('=' * 40)
print("Select The Type Of The Password")
print('=' * 40)

passTypes = [
    'Digits',
    'Lowercase Letters',
    'Uppercase Letters',
    'Special Characters',
    'Mix of All',
]

for index, value in enumerate(passTypes):
    print(f'{index + 1}: {value}')

print('=' * 40)

try:
    length = int(input("Enter the Length of the Password: "))
    print('=' * 40)
    option = input("Enter the Type of Password (1-5): ")
    print('=' * 40)

    if option == '1':
        chars = string.digits
    elif option == '2':
        chars = string.ascii_lowercase
    elif option == '3':
        chars = string.ascii_uppercase
    elif option == '4':
        chars = string.punctuation
    elif option == '5':
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid option selected. Please choose from 1 to 5.")
        exit()

    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number for length.")