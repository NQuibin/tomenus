from uuid import uuid4
from typing import Optional

from menus.transformer import menu_to_dto
from menus.dtos import MenuDTOv2
from .models import Restaurant
from .dtos import RestaurantDTO, CreateUpdateRestaurantPayloadDTO


def restaurant_to_dto(model: Restaurant) -> RestaurantDTO:
    if model.menu is None:
        menu = []
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


def restaurant_to_model(
    dto: CreateUpdateRestaurantPayloadDTO,
    restaurant_id: Optional[str] = None
) -> Restaurant:
    return Restaurant(
        id=restaurant_id or str(uuid4()),
        name=dto.name,
        primary_category=dto.primary_category,
        area=dto.area,
        description=dto.description,
        address1=dto.address1,
        address2=dto.address2,
        city=dto.city,
        province=dto.province,
        postal_code=dto.postal_code,
        country=dto.country,
        menu=[]
    )
