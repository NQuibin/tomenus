from uuid import uuid4
from datetime import datetime
from typing import Optional
from menus.models import Menu, MenuItem, MenuAddress
from menus.dtos import (
    MenuDTO,
    MenuItemDTO,
    MenuAddressDTO,
    CreateUpdateMenuPayloadDTO,
    CreateMenuItemPayloadDTO
)


def menu_address_to_dto(model: MenuAddress) -> MenuAddressDTO:
    return MenuAddressDTO(
        address1=model.address1,
        address2=model.address2,
        city=model.city,
        province=model.province,
        postal_code=model.postal_code,
        country=model.country
    )


def menu_address_to_model(dto: MenuAddressDTO) -> MenuAddress:
    return MenuAddress(
        address1=dto.address1,
        address2=dto.address2,
        city=dto.city,
        province=dto.province,
        postal_code=dto.postal_code,
        country=dto.country
    )


def menu_item_to_dto(model: MenuItem) -> MenuItemDTO:
    return MenuItemDTO(
        id=model.id,
        name=model.name,
        description=model.description,
        price=model.price
    )


def menu_item_to_model(dto: CreateMenuItemPayloadDTO) -> MenuItem:
    return MenuItem(
        id=str(uuid4()),
        name=dto.name,
        description=dto.description,
        price=dto.price
    )


def menu_to_dto(model: Menu) -> MenuDTO:
    if model.items is None:
        items = []
    else:
        items = [menu_item_to_dto(item) for item in model.items]

    return MenuDTO(
        id=model.id,
        name=model.name,
        primary_category=model.primary_category,
        area=model.area,
        status=model.status,
        description=model.description,
        address=menu_address_to_dto(model.address) if model.address else None,
        items=items,
        created_at=model.created_at.isoformat(),
        updated_at=model.updated_at.isoformat()
    )


def menu_to_model(dto: CreateUpdateMenuPayloadDTO, menu_id: Optional[str] = None) -> Menu:
    if dto.items is None:
        items = []
    else:
        items = [menu_item_to_model(item) for item in dto.items]

    return Menu(
        id=menu_id or str(uuid4()),
        name=dto.name,
        primary_category=dto.primary_category,
        area=dto.area,
        status=dto.status or 'ACTIVE',
        description=dto.description,
        address=dto.address.to_dict(),
        items=items,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
