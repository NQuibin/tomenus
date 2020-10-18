from typing import Optional
from uuid import uuid4

from menu_items.transformer import menu_item_to_dto
from .models import Menu
from .dtos import MenuDTOv2


def menu_to_dto(model: Menu) -> MenuDTOv2:
    if model.menu_items is None:
        menu_items = []
    else:
        menu_items = [menu_item_to_dto(menu_item) for menu_item in model.menu_items]

    return MenuDTOv2(
        id=str(model.id),
        restaurant_id=str(model.restaurant_id),
        name=model.name,
        description=model.description,
        menu_items=menu_items
    )


def menu_to_model(dto: MenuDTOv2, menu_id: Optional[str] = None) -> Menu:
    return Menu(
        id=menu_id or str(uuid4()),
        restaurant_id=dto.restaurant_id,
        name=dto.name,
        description=dto.description
    )
