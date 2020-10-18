from typing import List, Tuple
from .repository import MenusRepository
from .dtos import MenuDTO, CreateUpdateMenuPayloadDTO
from utils import menu_transformer
from .exceptions import MenuNotFound, MenuToUpdateNotFound, InvalidMenuItemPrice
from utils.validators import validate_positive_int


class MenusManager:
    def __init__(self):
        self.repository = MenusRepository()

    def _validate_menu_item_price(self, items: list):
        if items:
            for item in items:
                if item.price is not None and not validate_positive_int(item.price):
                    raise InvalidMenuItemPrice(item.name, item.price)

    def get_menu(self, menu_id: str) -> MenuDTO:
        menu = self.repository.get(menu_id)
        if menu is None:
            raise MenuNotFound(menu_id)
        return menu_transformer.menu_to_dto(menu)

    def get_menus(self, status: str, page_key: str, page_size: str) -> Tuple[List[MenuDTO], dict]:
        menus, next_page_key = self.repository.get_all(
            status=status,
            page_key=page_key,
            page_size=page_size
        )
        return [menu_transformer.menu_to_dto(menu) for menu in menus], next_page_key

    def create_menu(self, payload: CreateUpdateMenuPayloadDTO) -> MenuDTO:
        self._validate_menu_item_price(payload.items)

        menu = menu_transformer.menu_to_model(payload)
        new_menu = self.repository.save(menu)
        return menu_transformer.menu_to_dto(new_menu)

    def update_menu(self, menu_id: str, payload: CreateUpdateMenuPayloadDTO) -> MenuDTO:
        self._validate_menu_item_price(payload.items)

        menu = self.repository.get(menu_id)
        if menu is None:
            raise MenuToUpdateNotFound(menu_id)

        updated_menu = menu_transformer.menu_to_model(dto=payload, menu_id=menu_id)
        updated_menu = self.repository.save(updated_menu)
        return menu_transformer.menu_to_dto(updated_menu)
