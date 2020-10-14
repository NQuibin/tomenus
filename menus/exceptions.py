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


class InvalidMenuItemPrice(HttpEventHandlerException):
    def __init__(self, menu_name: str, price: Any):
        super().__init__(
            400,
            f'Menu item price is not a positive integer: {menu_name}, {str(price)}'
        )


class InvalidQueryParam(HttpEventHandlerException):
    def __init__(self, query_param: str, query_param_value: Any, message: str):
        super().__init__(
            400,
            f'Invalid query param - {message}: {query_param}, {query_param_value}'
        )
