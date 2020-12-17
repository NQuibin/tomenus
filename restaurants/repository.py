from db import establish_connection

from .models import Restaurant


class RestaurantRepository:
    def __init__(self):
        establish_connection()

    def save(self, model: Restaurant) -> Restaurant:
        model.address.save()
        return model.save(cascade=True)

    def get(self, restaurant_id: str) -> Restaurant:
        return Restaurant.objects.get(id=restaurant_id)
