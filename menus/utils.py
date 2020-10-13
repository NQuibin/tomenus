from uuid import uuid4
from datetime import datetime
from .dtos import (
    MenuDTO,
    MenuItemDTO,
    MenuAddressDTO,
    CreateMenuPayloadDTO,
    CreateMenuItemPayloadDTO
)
from .models import Menu, MenuItem, MenuAddress


def create_address_dto_from_model(model: MenuAddress) -> MenuAddressDTO:
    return MenuAddressDTO(
        address1=model.address1,
        address2=model.address2,
        city=model.city,
        province=model.province,
        postal_code=model.postal_code,
        country=model.country
    )


def create_menu_item_dto_from_model(model: MenuItem) -> MenuItemDTO:
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
        address=create_address_dto_from_model(model.address) if model.address else None,
        items=items,
        created_at=model.created_at.isoformat(),
        updated_at=model.updated_at.isoformat()
    )


def create_menu_item_model_from_dto(dto: CreateMenuItemPayloadDTO) -> MenuItem:
    return MenuItem(
        id=str(uuid4()),
        name=dto.name,
        price=dto.price
    )


def create_menu_model_from_dto(dto: CreateMenuPayloadDTO) -> Menu:
    if dto.items is None:
        items = []
    else:
        items = [create_menu_item_model_from_dto(item) for item in dto.items]

    return Menu(
        id=str(uuid4()),
        name=dto.name,
        primary_category=dto.primary_category,
        area=dto.area,
        address=dto.address,
        items=items,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
