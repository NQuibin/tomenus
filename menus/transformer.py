from typing import Optional
from uuid import uuid4

from menu_items.transformer import menu_item_to_dto, menu_item_to_model
from .models import Menu
from .dtos import MenuDTO, CreateUpdateMenuPayloadDTO


def menu_to_dto(model: Menu) -> MenuDTO:
    if model.menu_items is None:
        menu_items = []
    else:
        menu_items = [menu_item_to_dto(menu_item) for menu_item in model.menu_items]

    return MenuDTO(
        id=str(model.id),
        restaurant_id=str(model.restaurant_id),
        name=model.name,
        description=model.description,
        menu_items=menu_items,
        created_at=model.created_at.isoformat(),
        updated_at=model.updated_at.isoformat()
    )


def menu_to_model(
    dto: CreateUpdateMenuPayloadDTO,
    menu_id: Optional[str] = None
) -> Menu:
    if not dto.menu_items:
        menu_items = []
    else:
        menu_items = [menu_item_to_model(menu_item) for menu_item in dto.menu_items]

    return Menu(
        id=menu_id or str(uuid4()),
        name=dto.name,
        description=dto.description,
        menu_items=menu_items
    )
