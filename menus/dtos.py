from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin
from typing import List, Optional

from menu_items.dtos import MenuItemDTO


@dataclass
class MenuAddressDTO(DataClassJsonMixin):
    address1: str
    address2: str
    city: str
    province: str
    postal_code: str
    country: str


@dataclass
class MenuItemDTO(DataClassJsonMixin):
    id: str
    name: str
    description: Optional[str] = None
    price: Optional[int] = None


@dataclass
class MenuDTO(DataClassJsonMixin):
    id: str
    name: str
    primary_category: str
    area: str
    status: str
    description: Optional[str] = None
    address: Optional[MenuAddressDTO] = None
    items: List[MenuItemDTO] = field(default_factory=list)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


@dataclass
class CreateMenuItemPayloadDTO(DataClassJsonMixin):
    name: str
    description: Optional[str] = None
    price: Optional[int] = None


@dataclass
class CreateUpdateMenuPayloadDTO(DataClassJsonMixin):
    name: str
    primary_category: str
    area: str
    status: str
    description: Optional[str] = None
    address: Optional[MenuAddressDTO] = None
    items: List[CreateMenuItemPayloadDTO] = field(default_factory=list)


@dataclass
class MenuDTOv2(DataClassJsonMixin):
    id: str
    restaurant_id: str
    name: str
    description: Optional[str] = None
    menu_items: List[MenuItemDTO] = field(default_factory=list)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


@dataclass
class CreateUpdateMenuPayloadDTOv2(DataClassJsonMixin):
    restaurant_id: str
    name: str
    section: str
    section_order: int
    order: int
    description: Optional[str] = None
    price: Optional[int] = None
