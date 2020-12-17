from typing import Union, Any
from bson.objectid import ObjectId


def validate_uuid(oid: str) -> bool:
    return ObjectId.is_valid(oid)


def validate_oid(oid: str) -> bool:
    return ObjectId.is_valid(oid)


def validate_positive_int(price: Union[int, Any]) -> bool:
    if not isinstance(price, int):
        return False

    try:
        valid_int = int(price)
        return valid_int >= 0
    except ValueError:
        return False
