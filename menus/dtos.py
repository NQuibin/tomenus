from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin
from typing import List, Optional


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
    price: Optional[int]


@dataclass
class MenuDTO(DataClassJsonMixin):
    id: str
    name: str
    primary_category: str
    area: str
    address: Optional[MenuAddressDTO] = None
    items: List[MenuItemDTO] = field(default_factory=list)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


@dataclass
class CreateMenuItemPayloadDTO(DataClassJsonMixin):
    name: str
    price: Optional[int]


@dataclass
class CreateMenuPayloadDTO(DataClassJsonMixin):
    name: str
    primary_category: str
    area: str
    address: Optional[MenuAddressDTO] = None
    items: List[CreateMenuItemPayloadDTO] = field(default_factory=list)
