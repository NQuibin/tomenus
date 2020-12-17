from typing import Optional, List
from dataclasses import dataclass, field

from dataclasses_json import DataClassJsonMixin


@dataclass
class AddressDTO(DataClassJsonMixin):
    id: str
    address1: str
    city: str
    province: str
    code: str
    country: str
    address2: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


@dataclass
class RestaurantDTO(DataClassJsonMixin):
    id: str
    name: str
    primary_category: str
    status: str
    address: AddressDTO
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


@dataclass
class CreateUpdateAddressPayloadDTO(DataClassJsonMixin):
    address1: str
    city: str
    province: str
    code: str
    country: str
    address2: Optional[str] = None


@dataclass
class CreateUpdateRestaurantPayloadDTO(DataClassJsonMixin):
    name: str
    primary_category: str
    status: str
    address: CreateUpdateAddressPayloadDTO
    description: Optional[str] = None
