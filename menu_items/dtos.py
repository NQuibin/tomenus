from typing import Optional
from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin


@dataclass
class MenuItemDTO(DataClassJsonMixin):
    id: str
    menu_id: str
    name: str
    section: str
    section_order: int
    order: int
    description: Optional[str] = None
    price: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
