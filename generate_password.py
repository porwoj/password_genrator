import secrets
import string
import sys
import argparse

parser = argparse.ArgumentParser()
letters = string.ascii_letters
parser.add_argument('-c','--chars',dest='chars',choices=['letters','digits','specials'],default=['letters','digits','specials'],nargs='+',help='Character sets use for password generate. Mix options allowed separated by space.')
parser.add_argument('-l','--length',dest='length',default=12,type=int,help='Password lenngth, any integer value.')

args=parser.parse_args()

letters = string.ascii_letters
digits = string.digits
specials = string.punctuation

chars_pot=''
for sub in args.chars:
    if sub == 'letters':
        chars_pot += letters
    if sub == 'digits':
        chars_pot += digits
    if sub == 'specials':
        chars_pot += specials

password=''
for i in range(args.length):
    password += ''.join(secrets.choice(chars_pot))

print(password)
