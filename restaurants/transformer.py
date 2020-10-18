from .models import Restaurant
from .dtos import RestaurantDTO


def restaurant_to_dto(model: Restaurant) -> RestaurantDTO:
    return RestaurantDTO(
        id=str(model.id),
        name=model.name,
        primary_category=model.primary_category,
        area=model.area,
        description=model.description,
        address1=model.address1,
        address2=model.address2,
        city=model.city,
        province=model.province,
        postal_code=model.postal_code,
        country=model.country
    )
