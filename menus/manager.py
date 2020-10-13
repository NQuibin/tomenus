from typing import List
from .repository import MenusRepository
from .dtos import MenuDTO, CreateMenuPayloadDTO
from .utils import create_menu_dto_from_model, create_menu_model_from_dto
from .exceptions import MenuNotFound, InvalidMenuItemPrice
from .validators import validate_price


class MenusManager:
    def __init__(self):
        self.repository = MenusRepository()

    def get_menu(self, menu_id: str) -> MenuDTO:
        menu = self.repository.get(menu_id)
        if menu is None:
            raise MenuNotFound(menu_id)
        return create_menu_dto_from_model(menu)

    def get_menus(self) -> List[MenuDTO]:
        menus = self.repository.get_all()
        return [create_menu_dto_from_model(menu) for menu in menus]

    def create_menu(self, payload: CreateMenuPayloadDTO) -> MenuDTO:
        if payload.items:
            for item in payload.items:
                if not validate_price(item.price):
                    raise InvalidMenuItemPrice(item.name, item.price)

        menu = create_menu_model_from_dto(payload)
        new_menu = self.repository.create(menu)
        return create_menu_dto_from_model(new_menu)
