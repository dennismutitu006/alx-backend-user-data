#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        '''creates and adds a user to the db and returns user object.
        '''
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by arbitrary keyword args.
        """
        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found with the given criteria")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid request with the given ")

    def update_user(self, user_id: int, **kwargs) -> None:
        """func updates the user table.
        """
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if not hasattr(user, key):
                    raise ValueError("Error")
                setattr(user, key, value)
            self._session.commit()
        except NoResultFound:
            raise NoResultFound(f"No user found with id {user_id}")
        except InvalidRequestError:
            raise InvalidRequestError(f"Invalid request with id {user_id}")
