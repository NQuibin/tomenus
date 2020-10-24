from typing import List, Optional

from .repository import MenuItemRepository
from .dtos import MenuItemDTO, CreateUpdateMenuItemPayloadDTO
from .models import MenuItem
from .transformer import menu_item_to_dto, menu_item_to_model
from .exceptions import MenuItemNotFound


class MenuItemManager:
    def __init__(self):
        self.repository = MenuItemRepository()

    def get_menu_item(self, menu_item_id: str) -> MenuItemDTO:
        menu_item = self.repository.get(MenuItem, MenuItem.id == menu_item_id)
        if menu_item is None:
            raise MenuItemNotFound(menu_item_id)
        return menu_item_to_dto(menu_item)

    def get_menu_items(self, page_key: str, page_size: str) -> (List[MenuItemDTO], Optional[str]):
        menu_items, next_page_key = self.repository.get_all(
            model_class=MenuItem,
            page_key=int(page_key),
            page_size=int(page_size)
        )
        return [menu_item_to_dto(menu_item) for menu_item in menu_items], next_page_key

    def create_menu_item(self, payload: CreateUpdateMenuItemPayloadDTO) -> MenuItemDTO:
        menu_item = menu_item_to_model(payload)
        new_menu_item = self.repository.create(menu_item)
        return menu_item_to_dto(new_menu_item)

    def update_menu_item(self, menu_item_id: str, payload: CreateUpdateMenuItemPayloadDTO) -> MenuItemDTO:
        menu_item = menu_item_to_model(dto=payload, menu_item_id=menu_item_id)
        updated_menu_item = self.repository.update(menu_item)
        return menu_item_to_dto(updated_menu_item)
