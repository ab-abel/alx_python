#!/usr/bin/env python3
#validate password from users

def check_for_int(word):
    a = []
    for i in word:
        if(i.isdigit()):
            a.append(i)
    if(len(a)>=1):
        is_valid = True
    else:
        is_valid = False
    return is_valid

def check_white_space(word):
    a = []
    for i in word:
        if(i.isspace()):
            a.append(i)
    if(len(a)>=1):
        is_valid = True
    else:
        is_valid = False
    return is_valid

def validate_password(password:str):
    is_valid = False
    if (len(password)>=8 and not password.islower() 
        and not password.isupper() 
        and check_for_int(password) 
        and not check_white_space(password)):

        is_valid = True
    else:
        is_valid = False
    return is_valid

print(validate_password('oajdsah9D'))
