from uuid import uuid4
from typing import Optional

from menus.transformer import menu_to_dto, menu_to_model
from .models import Restaurant
from .dtos import RestaurantDTO, CreateUpdateRestaurantPayloadDTO


def restaurant_to_dto(model: Restaurant) -> RestaurantDTO:
    if model.menus is None:
        menus = []
    else:
        menus = [menu_to_dto(menu_model) for menu_model in model.menus]

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
        menus=menus,
        created_at=model.created_at.isoformat(),
        updated_at=model.updated_at.isoformat()
    )


def restaurant_to_model(
    dto: CreateUpdateRestaurantPayloadDTO,
    restaurant_id: Optional[str] = None
) -> Restaurant:
    if not dto.menus:
        menus = []
    else:
        menus = [menu_to_model(menu) for menu in dto.menus]

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
        menus=menus
    )
