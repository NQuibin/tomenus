from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin
from typing import List, Optional


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
    location: str
    items: List[MenuItemDTO] = field(default_factory=list)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


@dataclass
class CreateMenuPayloadDTO(DataClassJsonMixin):
    name: str
    primary_category: str
    area: str
    location: str
    items: List[MenuItemDTO] = field(default_factory=list)
