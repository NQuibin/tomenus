from typing import List, Optional

from db.db_api import DbApi
from .models import Restaurant


class RestaurantRepository:
    def __init__(self):
        self.db = DbApi()

    def get_restaurant(self, restaurant_id: str) -> Restaurant:
        with self.db.session_local(expire_on_commit=False) as session:
            return session.query(Restaurant) \
                .filter(Restaurant.id == restaurant_id) \
                .first()

    def get_restaurants(
        self,
        page_key: int,
        page_size: int
    ) -> (List[Restaurant], Optional[str]):
        with self.db.session_local(expire_on_commit=False) as session:
            offset = (page_key - 1) * page_size
            restaurants = session.query(Restaurant) \
                .order_by(Restaurant.created_at) \
                .limit(page_size) \
                .offset(offset) \
                .all()
            total = session.query(Restaurant).count()

            next_page_key = str(page_key + 1) if offset + len(restaurants) < total else None
            return restaurants, next_page_key

    def create_restaurant(self, model: Restaurant) -> Restaurant:
        with self.db.session_local(expire_on_commit=False) as session:
            session.add(model)
            return model
