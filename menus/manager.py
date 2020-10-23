from typing import Union

from .repository import MenuRepository
from .dtos import MenuDTO, MenuDTOFull
from .transformer import menu_to_dto
from .exceptions import MenuNotFound


class MenuManager:
    def __init__(self):
        self.repository = MenuRepository()

    def get_menu(self, menu_id: str, full: bool = False) -> Union[MenuDTO, MenuDTOFull]:
        menu = self.repository.get_menu(menu_id)
        if menu is None:
            raise MenuNotFound(menu_id)
        return menu_to_dto(model=menu, full=full)
