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
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        '''public method that returns none-request will be th flask req obj'''
        pass

    def current_user(self, request=None) -> TypeVar('User'):
        '''returns None-request will be the flask request obj'''
        pass
