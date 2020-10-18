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
