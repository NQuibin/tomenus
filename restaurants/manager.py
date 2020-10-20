from typing import List, Optional

from .repository import RestaurantRepository
from .transformer import restaurant_to_dto, restaurant_to_model
from .dtos import RestaurantDTO, CreateUpdateRestaurantPayloadDTO
from .exceptions import RestaurantNotFound


class RestaurantManager:
    def __init__(self):
        self.repository = RestaurantRepository()

    def get_restaurant(self, restaurant_id: str, is_minimal: bool = False) -> RestaurantDTO:
        restaurant = self.repository.get_restaurant(restaurant_id)
        if restaurant is None:
            raise RestaurantNotFound(restaurant_id)
        return restaurant_to_dto(model=restaurant, is_minimal=is_minimal)

    def get_restaurants(
        self,
        page_key: str,
        page_size: str
    ) -> (List[RestaurantDTO], Optional[str]):
        restaurants, next_page_key = self.repository.get_restaurants(
            page_key=int(page_key),
            page_size=int(page_size)
        )
        return [restaurant_to_dto(restaurant) for restaurant in restaurants], next_page_key

    def create_restaurant(self, payload: CreateUpdateRestaurantPayloadDTO) -> RestaurantDTO:
        restaurant = restaurant_to_model(payload)
        new_restaurant = self.repository.create_restaurant(restaurant)
        return restaurant_to_dto(new_restaurant)
