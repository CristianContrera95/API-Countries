from fastapi import HTTPException


class BadFilterException(HTTPException):
    def __init__(self, message=None, status_code=400):
        super().__init__(status_code=status_code, detail=message)


class SortByException(HTTPException):
    def __init__(self, message=None, status_code=400):
        super().__init__(status_code=status_code, detail=message)
