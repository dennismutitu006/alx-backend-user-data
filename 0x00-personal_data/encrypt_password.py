#!/usr/bin/env python3
'''encrypting passwords using bcrypt'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''function takes a string arg and returns a salted
    hashed password which is a byte string.
    '''
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
