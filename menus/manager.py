from typing import Union, List, Optional

from .repository import MenuRepository
from .dtos import MenuDTO, MenuDTOFull, CreateUpdateMenuPayloadDTO
from .models import Menu
from .transformer import menu_to_dto, menu_to_model
from .exceptions import MenuNotFound


class MenuManager:
    def __init__(self):
        self.repository = MenuRepository()

    def get_menu(self, menu_id: str, full: bool = False) -> Union[MenuDTO, MenuDTOFull]:
        menu = self.repository.get(Menu, Menu.id == menu_id)
        if menu is None:
            raise MenuNotFound(menu_id)
        return menu_to_dto(model=menu, full=full)

    def get_menus(
        self,
        page_key: str,
        page_size: str,
        full: bool = False
    ) -> (List[Union[MenuDTO, MenuDTOFull]], Optional[str]):
        menus, next_page_key = self.repository.get_all(
            model_class=Menu,
            page_key=int(page_key),
            page_size=int(page_size)
        )
        return [menu_to_dto(model=menu, full=full) for menu in menus], next_page_key

    def create_menu(self, payload: CreateUpdateMenuPayloadDTO) -> MenuDTO:
        menu = menu_to_model(payload)
        new_menu = self.repository.create(menu)
        return menu_to_dto(new_menu)

    def update_menu(self, menu_id: str, payload: CreateUpdateMenuPayloadDTO) -> MenuDTO:
        menu = menu_to_model(dto=payload, menu_id=menu_id)
        updated_menu = self.repository.update(menu)
        return menu_to_dto(updated_menu)
