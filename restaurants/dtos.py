from typing import Optional, List
from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin

from menus.dtos import MenuDTOv2


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
    menu: Optional[List[MenuDTOv2]] = None
