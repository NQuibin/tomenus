from utils.http_events import (
    Request,
    Response,
    parse_http_event,
    global_exception
)
from utils.validators import validate_uuid
from .manager import RestaurantManager
from .exceptions import InvalidRestaurantId
from .dtos import CreateUpdateRestaurantPayloadDTO

manager = RestaurantManager()


@global_exception
@parse_http_event
def get_restaurant(request: Request):
    restaurant_id = request.path_params.get('id')
    if not validate_uuid(restaurant_id):
        raise InvalidRestaurantId(restaurant_id)

    restaurant = manager.get_restaurant(restaurant_id)
    return Response(status_code=200, message_body=restaurant).to_dict()


@global_exception
@parse_http_event
def get_restaurants(_: Request):
    return Response(status_code=200, message_body='Not implemented').to_dict()


@global_exception
@parse_http_event
def create_restaurant(request: Request):
    payload = CreateUpdateRestaurantPayloadDTO.from_dict(request.body)
    restaurant = manager.create_restaurant(payload)
    return Response(status_code=200, message_body=restaurant).to_dict()
