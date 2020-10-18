from .repository import RestaurantRepository
from .transformer import restaurant_to_dto
from .dtos import RestaurantDTO


class RestaurantManager:
    def __init__(self):
        self.repository = RestaurantRepository()

    def get_restaurant(self, restaurant_id: str) -> RestaurantDTO:
        restaurant = self.repository.get_restaurant(restaurant_id)
        return restaurant_to_dto(restaurant)
