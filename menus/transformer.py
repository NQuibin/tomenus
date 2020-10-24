from typing import Optional, Union
from uuid import uuid4

from menu_items.transformer import menu_item_to_dto
from .models import Menu
from .dtos import MenuDTO, MenuDTOFull, CreateUpdateMenuPayloadDTO


def menu_to_dto(model: Menu, full: bool = False) -> Union[MenuDTO, MenuDTOFull]:
    args = {
        'id': str(model.id),
        'restaurant_id': str(model.id),
        'name': model.name,
        'description': model.description,
        'created_at': model.created_at.isoformat(),
        'updated_at': model.updated_at.isoformat()
    }

    if full:
        args['menu_items'] = [] \
            if model.menu_items is None \
            else [menu_item_to_dto(menu_item_model) for menu_item_model in model.menu_items]

        return MenuDTOFull(**args)

    return MenuDTO(**args)


def menu_to_model(
    dto: CreateUpdateMenuPayloadDTO,
    menu_id: Optional[str] = None
) -> Menu:
    return Menu(
        id=menu_id or str(uuid4()),
        restaurant_id=dto.restaurant_id,
        name=dto.name,
        description=dto.description
    )
