from typing import Optional
from uuid import uuid4

from .models import MenuItem
from .dtos import MenuItemDTO, CreateUpdateMenuItemPayloadDTO


def menu_item_to_dto(model: MenuItem) -> MenuItemDTO:
    return MenuItemDTO(
        id=str(model.id),
        menu_id=str(model.menu_id),
        name=model.name,
        section=model.section,
        section_order=model.section_order,
        order=model.order,
        description=model.description,
        price=model.price,
        created_at=model.created_at.isoformat(),
        updated_at=model.updated_at.isoformat()
    )


def menu_item_to_model(
    dto: CreateUpdateMenuItemPayloadDTO,
    menu_item_id: Optional[str] = None
) -> MenuItem:
    return MenuItem(
        id=menu_item_id or str(uuid4()),
        menu_id=dto.menu_id,
        name=dto.name,
        section=dto.section,
        section_order=dto.section_order,
        order=dto.order,
        description=dto.description,
        price=dto.price
    )
