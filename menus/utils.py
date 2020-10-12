from .dtos import MenuDTO, MenuItemDTO
from .models import Menu


def create_menu_item_dto_from_model(model: MenuItemDTO) -> MenuItemDTO:
    return MenuItemDTO(
        id=model.id,
        name=model.name,
        price=model.price
    )


def create_menu_dto_from_model(model: Menu) -> MenuDTO:
    if model.items is None:
        items = []
    else:
        items = [create_menu_item_dto_from_model(item) for item in model.items]

    return MenuDTO(
        id=model.id,
        name=model.name,
        primary_category=model.primary_category,
        area=model.area,
        location=model.location,
        items=items,
        createdAt=str(model.created_at),
        updatedAt=str(model.updated_at)
    )


