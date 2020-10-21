from uuid import uuid4
from typing import Optional, Union

from menus.transformer import menu_to_dto, menu_to_model
from .models import Restaurant
from .dtos import RestaurantDTO, RestaurantDTOFull, CreateUpdateRestaurantPayloadDTO


def restaurant_to_dto(model: Restaurant, full: bool = False) -> Union[RestaurantDTO, RestaurantDTOFull]:
    menus = [] \
        if not full or model.menus is None \
        else [menu_to_dto(menu_model) for menu_model in model.menus]

    args = {
        'id': str(model.id),
        'name': model.name,
        'primary_category': model.primary_category,
        'area': model.area,
        'description': model.description,
        'address1': model.address1,
        'address2': model.address2,
        'city': model.city,
        'province': model.province,
        'postal_code': model.postal_code,
        'country': model.country,
        'created_at': model.created_at.isoformat(),
        'updated_at': model.updated_at.isoformat()
    }
    if full:
        args['menus'] = menus

    return RestaurantDTOFull(**args) if full else RestaurantDTO(**args)


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
        country=dto.country
    )
