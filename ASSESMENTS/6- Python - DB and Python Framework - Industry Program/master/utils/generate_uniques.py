import random
import string

def generate_password(digit=8):
    ch = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = ''
    for i in range(digit):
        password += random.choice(ch)
    return password


def generate_otp(digit=6):
    ch = string.digits
    otp = ''
    for i in range(digit):
        otp += random.choice(ch)
    return otp

