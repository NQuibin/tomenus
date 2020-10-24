from typing import List, Optional

from db import DbApi, BaseRepository
from .models import Restaurant


class RestaurantRepository(BaseRepository):
    def __init__(self):
        super().__init__(DbApi())

    def get_restaurant(self, restaurant_id: str) -> Restaurant:
        return self.get(Restaurant, Restaurant.id == restaurant_id)

    def get_restaurants(
        self,
        page_key: int,
        page_size: int
    ) -> (List[Restaurant], Optional[int]):
        return self.get_all(model_class=Restaurant, page_key=page_key, page_size=page_size)

    def create_restaurant(self, model: Restaurant) -> Restaurant:
        return self.create(model)

    def update_restaurant(self, model: Restaurant) -> Restaurant:
        return self.update(model)
