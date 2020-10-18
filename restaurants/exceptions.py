from utils.exceptions import HttpEventHandlerException


class InvalidRestaurantId(HttpEventHandlerException):
    def __init__(self, restaurant_id: str):
        super().__init__(400, f'Invalid restaurant id: {restaurant_id}')
