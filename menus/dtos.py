from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional


@dataclass_json
@dataclass
class MenuItemDTO:
    id: str
    name: str
    price: Optional[int]


@dataclass_json
@dataclass
class MenuDTO:
    id: str
    name: str
    primary_category: Optional[str]
    area: Optional[str]
    location: Optional[str]
    items: List[MenuItemDTO] = field(default_factory=list)
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
