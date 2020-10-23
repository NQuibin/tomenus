from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin
from typing import List, Optional

from menu_items.dtos import MenuItemDTO, CreateUpdateMenuItemPayloadDTO


@dataclass
class MenuDTO(DataClassJsonMixin):
    id: str
    restaurant_id: str
    name: str
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


@dataclass
class MenuDTOFull(MenuDTO, DataClassJsonMixin):
    menu_items: List[MenuItemDTO] = field(default_factory=list)


@dataclass
class CreateUpdateMenuPayloadDTO(DataClassJsonMixin):
    name: str
    description: Optional[str] = None
    price: Optional[int] = None
    menu_items: List[CreateUpdateMenuItemPayloadDTO] = field(default_factory=list)
