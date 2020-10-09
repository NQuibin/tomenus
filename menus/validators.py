from uuid import UUID


def validate_uuid(uuid: str) -> bool:
    try:
        UUID(uuid)
        return True
    except ValueError:
        return False
