from utils.exceptions import HttpEventHandlerException


class InvalidMenuId(HttpEventHandlerException):
    def __init__(self, menu_id: str):
        super().__init__(400, f'Invalid menu id: {menu_id}')


class MenuNotFound(HttpEventHandlerException):
    def __init__(self, menu_id: str):
        super().__init__(404, f'Menu not found: {menu_id}')
