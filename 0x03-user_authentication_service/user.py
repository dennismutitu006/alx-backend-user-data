#!/usr/bin/env python3
'''creating an SQLALchemy model named User'''
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    '''the class User for a db table named users
    the instances will be the rows of the table.
    '''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        '''to provide a convinent str rep of user objects'''
        return (f"< User(id={self.id}, email={self.email},"
                f"hashed_password={self.hashed_password},"
                f"session_id={self.session_id},"
                f"reset_token={self.reset_token}) >")
