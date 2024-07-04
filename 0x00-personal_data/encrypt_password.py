#!/usr/bin/env python3
'''encrypting passwords using bcrypt'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''function takes a string arg and returns a salted
    hashed password which is a byte string.
    '''
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''use bcrypt to validate that the provided passwrds macht hashed'''
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
