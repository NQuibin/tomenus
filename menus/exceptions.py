from typing import Any


class HttpEventHandlerException(Exception):
    def __init__(self, status_code: int, message: Any):
        super().__init__(str(message))
        self.statusCode = status_code
        self.message = message


class InvalidMenuId(HttpEventHandlerException):
    def __init__(self, menu_id: str):
        super().__init__(400, f'Invalid id: {menu_id}')


class MenuNotFound(HttpEventHandlerException):
    def __init__(self, menu_id: str):
        super().__init__(404, f'Menu not found: {menu_id}')
