from .repository import RestaurantRepository
from .transformer import restaurant_to_dto, restaurant_to_model
from .dtos import RestaurantDTO, CreateUpdateRestaurantPayloadDTO
from .exceptions import RestaurantNotFound


class RestaurantManager:
    def __init__(self):
        self.repository = RestaurantRepository()

    def get_restaurant(self, restaurant_id: str) -> RestaurantDTO:
        restaurant = self.repository.get_restaurant(restaurant_id)
        if restaurant is None:
            raise RestaurantNotFound(restaurant_id)
        return restaurant_to_dto(restaurant)

    def create_restaurant(self, payload: CreateUpdateRestaurantPayloadDTO) -> RestaurantDTO:
        restaurant = restaurant_to_model(payload)
        new_restaurant = self.repository.create_restaurant(restaurant)
        return restaurant_to_dto(new_restaurant)
