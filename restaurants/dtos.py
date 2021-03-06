from typing import Optional, List
from dataclasses import dataclass, field

from dataclasses_json import DataClassJsonMixin

from menus.dtos import MenuDTO


@dataclass
class RestaurantDTO(DataClassJsonMixin):
    id: str
    name: str
    primary_category: str
    area: str
    description: Optional[str] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


@dataclass
class RestaurantDTOFull(RestaurantDTO, DataClassJsonMixin):
    menus: List[MenuDTO] = field(default_factory=list)


@dataclass
class CreateUpdateRestaurantPayloadDTO(DataClassJsonMixin):
    name: str
    primary_category: str
    area: str
    description: Optional[str] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
