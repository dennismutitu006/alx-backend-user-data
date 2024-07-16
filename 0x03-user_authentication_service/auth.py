#!/usr/bin/env python3
''' hash password method '''
import bcrypt


def _hash_password(password: str) -> bytes:
    '''this method will use gensalt to generated a salted hash of the
    input password and return the bytes.
    '''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
