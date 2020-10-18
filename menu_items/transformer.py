from .models import MenuItem
from .dtos import MenuItemDTO


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
