from typing import List
from .repository import MenusRepository
from .dtos import MenuDTO, CreateMenuPayloadDTO
from .utils import menu_transformer
from .exceptions import MenuNotFound, InvalidMenuItemPrice
from .validators import validate_price


class MenusManager:
    def __init__(self):
        self.repository = MenusRepository()

    def get_menu(self, menu_id: str) -> MenuDTO:
        menu = self.repository.get(menu_id)
        if menu is None:
            raise MenuNotFound(menu_id)
        return menu_transformer.menu_to_dto(menu)

    def get_menus(self) -> List[MenuDTO]:
        menus = self.repository.get_all()
        return [menu_transformer.menu_to_dto(menu) for menu in menus]

    def create_menu(self, payload: CreateMenuPayloadDTO) -> MenuDTO:
        if payload.items:
            for item in payload.items:
                if item.price is not None and not validate_price(item.price):
                    raise InvalidMenuItemPrice(item.name, item.price)

        menu = menu_transformer.menu_to_model(payload)
        new_menu = self.repository.create(menu)
        return menu_transformer.menu_to_dto(new_menu)
