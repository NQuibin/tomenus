from typing import Optional

from .models import Restaurant, Address
from .dtos import (
    RestaurantDTO,
    AddressDTO,
    CreateUpdateRestaurantPayloadDTO,
    CreateUpdateAddressPayloadDTO
)


def address_to_dto(model: Address) -> AddressDTO:
    return AddressDTO(
        id=str(model.id),
        address1=model.address1,
        address2=model.address2,
        city=model.city,
        province=model.province,
        code=model.code,
        country=model.country,
        created_at=model.created_at.isoformat(),
        updated_at=model.updated_at.isoformat()
    )


def restaurant_to_dto(model: Restaurant) -> RestaurantDTO:
    args = {
        'id': str(model.id),
        'name': model.name,
        'primary_category': model.primary_category,
        'status': model.status,
        'description': model.description,
        'address': address_to_dto(model.address),
        'created_at': model.created_at.isoformat(),
        'updated_at': model.updated_at.isoformat()
    }
    return RestaurantDTO(**args)


def address_to_model(dto: CreateUpdateAddressPayloadDTO) -> Address:
    return Address(
        address1=dto.address1,
        address2=dto.address2,
        city=dto.city,
        province=dto.province,
        code=dto.code,
        country=dto.country
    )


def restaurant_to_model(dto: CreateUpdateRestaurantPayloadDTO) -> Restaurant:
    return Restaurant(
        name=dto.name,
        status=dto.status,
        primary_category=dto.primary_category,
        description=dto.description,
        address=address_to_model(dto.address)
    )
