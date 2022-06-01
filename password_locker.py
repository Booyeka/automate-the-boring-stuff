#! python3

#password_locker.py - insecure program to store passwords
import random
import string
import sys
import pyperclip

'''
if len(sys.argv) < 2:
    print('Usage: python password_locker.py [account] - copy account password')
    sys.exit()
'''

account = input()
#sys.argv[1] # first command line arg is the account name


def generate_pass():
    tot_string = string.ascii_letters + string.digits + string.punctuation
    password = ''
    pass_length = 16
    for i in range(pass_length):
        password += tot_string[random.randint(0,len(tot_string)-1)]
    return password

x = generate_pass()
y = generate_pass()
z = generate_pass()


password_dict = {
    'twitter': x,
    'myspace': y,
    'facebook': z,
    'gamail': '',
}

if account in password_dict:
    pyperclip.copy(password_dict[account])
    print(f'password for {account} copied to clipboard')
else:
    print(f'There is no account named {account}.')



