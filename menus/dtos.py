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
