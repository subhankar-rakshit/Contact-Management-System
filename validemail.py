'''This module checks a given email id is valid or not
and returns the status'''
import re

def IsValidEmail(email):
    emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # Username
    @                       # @Symbol
    [a-zA-Z0-9.-]+          # Domain Name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)

    email_address = emailRegex.findall(email)
    if len(email_address) != 0:
        return True
    else:
        return False