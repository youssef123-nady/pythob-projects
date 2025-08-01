# Create Random Username

import string
import random

prefix = ['user', 'dev', 'code', 'joo']

# k: means select 4 characters 
suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))

# concatenate the prefix and suffix
username = random.choice(prefix) + "_" + suffix

print('='*15)
print(username)
print('='*15)
