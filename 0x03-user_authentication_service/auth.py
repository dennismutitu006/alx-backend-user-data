#!/usr/bin/env python3
''' hash password method '''
import bcrypt
from user import User
from db import DB
import uuid
from sqlalchemy.orm.exc import NoResultFound


def _generate_uuid() -> str:
    '''generate universary unique identifier.'''
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    '''this method will use gensalt to generated a salted hash of the
    input password and return the bytes.
    '''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


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

    def valid_login(self, email: str, password: str) -> bool:
        '''credentials validation'''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode(),
                                      user.hashed_password.encode())
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        '''Create a new session for user and return session_id'''
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
