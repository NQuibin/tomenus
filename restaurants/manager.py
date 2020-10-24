from typing import List, Optional, Union

from .repository import RestaurantRepository
from .transformer import restaurant_to_dto, restaurant_to_model
from .dtos import RestaurantDTO, RestaurantDTOFull, CreateUpdateRestaurantPayloadDTO
from .models import Restaurant
from .exceptions import RestaurantNotFound


class RestaurantManager:
    def __init__(self):
        self.repository = RestaurantRepository()

    def get_restaurant(self, restaurant_id: str, full: bool = False) -> Union[RestaurantDTO, RestaurantDTOFull]:
        restaurant = self.repository.get(Restaurant, Restaurant.id == restaurant_id)
        if restaurant is None:
            raise RestaurantNotFound(restaurant_id)
        return restaurant_to_dto(model=restaurant, full=full)

    def get_restaurants(
        self,
        page_key: str,
        page_size: str,
        full: bool = False
    ) -> (List[Union[RestaurantDTO, RestaurantDTOFull]], Optional[str]):
        restaurants, next_page_key = self.repository.get_all(
            model_class=Restaurant,
            page_key=int(page_key),
            page_size=int(page_size)
        )
        return [restaurant_to_dto(model=restaurant, full=full) for restaurant in restaurants], next_page_key

    def create_restaurant(self, payload: CreateUpdateRestaurantPayloadDTO) -> RestaurantDTO:
        restaurant = restaurant_to_model(payload)
        new_restaurant = self.repository.create(restaurant)
        return restaurant_to_dto(new_restaurant)

    def update_restaurant(
        self,
        restaurant_id: str,
        payload: CreateUpdateRestaurantPayloadDTO
    ) -> RestaurantDTO:
        restaurant = restaurant_to_model(dto=payload, restaurant_id=restaurant_id)
        updated_restaurant = self.repository.update(restaurant)
        return restaurant_to_dto(updated_restaurant)
