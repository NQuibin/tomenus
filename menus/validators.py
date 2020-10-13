from uuid import UUID
from typing import Union, Any


def validate_uuid(uuid: str) -> bool:
    try:
        UUID(uuid)
        return True
    except ValueError:
        return False


def validate_price(price: Union[int, Any]) -> bool:
    if not isinstance(price, int):
        return False

    try:
        valid_price = int(price)
        return valid_price >= 0
    except ValueError:
        return False
