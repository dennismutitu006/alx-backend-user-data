#!/usr/bin/env python3
'''auth class'''
from flask import request
from typing import Tuple, List, TypeVar


class Auth:
    '''class manages the API authentication'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''public method that takes args and returns a bool false
        path and excluded_paths.
        '''
        pass


    def authorization_header(self, request=None) -> str:
        '''public method that returns none-request will be th flask req obj'''
        pass


    def current_user(self, request=None) -> TypeVar('User'):
        '''returns None-request will be the flask request obj'''
        pass
