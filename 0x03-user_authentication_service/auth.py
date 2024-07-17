#!/usr/bin/env python3
''' hash password method '''
import bcrypt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''Register a new user with the email and password'''
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            hashed_password = _hash_password(password)
            n_user = self._db.add_user(email, hashed_password.decode('utf-8'))
            return n_user


def _hash_password(password: str) -> bytes:
    '''this method will use gensalt to generated a salted hash of the
    input password and return the bytes.
    '''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def valid_login(self, email: str, password: str) -> bool:
    '''credentials validation'''
    try:
        user = self._db.find_user_by(email=email)
        return bcrypt.checkpw(password.encode('utf-8'),
                              user.hashed_password('utf-8'))
    except NoResultFound:
        return False
