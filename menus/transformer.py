from .models import Menu
from .dtos import MenuDTOv2


def menu_to_dto(model: Menu) -> MenuDTOv2:
    return MenuDTOv2(
        id=str(model.id),
        restaurant_id=str(model.restaurant_id),
        name=model.name,
        section=model.section,
        section_order=model.section_order,
        order=model.order,
        description=model.description,
        price=model.price
    )
