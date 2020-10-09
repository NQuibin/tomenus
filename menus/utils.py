from .dtos import MenuDTO
from .models import Menu


def create_menu_dto_from_model(model: Menu) -> MenuDTO:
    return MenuDTO(
        id=model.id,
        name=model.name,
        primary_category=model.primary_category,
        area=model.area,
        location=model.location,
        items=model.items,
        createdAt=str(model.created_at),
        updatedAt=str(model.updated_at)
    )
