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

    def get_user_from_session_id(self, session_id: str) -> User:
        '''Find user by session ID'''
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        '''this func will destroy a sesion'''
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """function takes an email arg and returns a string."""
        try:
            user = self._db.find_user_by(email=email)
            if not user or user is None:
                raise ValueError("User not found")

            reset_token = _generate_uuid()
            user.reset_token = reset_token
        except NoResultFound:
            raise ValueError(f"User {email} does not exist")
        else:
            return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """update password function.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user_id, hashed_password=hashed_password,
                                 reset_token=None)
            return None
        except Exception:
            raise ValueError
