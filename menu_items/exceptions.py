from utils.exceptions import HttpEventHandlerException


class InvalidMenuItemId(HttpEventHandlerException):
    def __init__(self, menu_id: str):
        super().__init__(400, f'Invalid Menu Item id: {menu_id}')


class MenuItemNotFound(HttpEventHandlerException):
    def __init__(self, menu_id: str):
        super().__init__(404, f'Menu Item not found: {menu_id}')
