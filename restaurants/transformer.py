from menus.dtos import MenuDTOv2
from menus.transformer import menu_to_dto
from .models import Restaurant
from .dtos import RestaurantDTO


def restaurant_to_dto(model: Restaurant) -> RestaurantDTO:
    if model.menu is None:
        menu = None
    else:
        menu = [menu_to_dto(menu_model) for menu_model in model.menu]

    return RestaurantDTO(
        id=str(model.id),
        name=model.name,
        primary_category=model.primary_category,
        area=model.area,
        description=model.description,
        address1=model.address1,
        address2=model.address2,
        city=model.city,
        province=model.province,
        postal_code=model.postal_code,
        country=model.country,
        menu=menu
    )
