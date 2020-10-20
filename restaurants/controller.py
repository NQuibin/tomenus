from werkzeug.http import parse_options_header

from utils.http.events import (
    Request,
    Response,
    PaginatedResponse,
    parse_http_event,
    global_exception
)
from utils.http.constants import PREFER_HEADER_RETURN_MINIMAL
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

    prefer_header = parse_options_header(request.headers.get('Prefer'))
    is_minimal = prefer_header[0] == PREFER_HEADER_RETURN_MINIMAL

    restaurant = manager.get_restaurant(restaurant_id=restaurant_id, is_minimal=is_minimal)
    return Response(status_code=200, message_body=restaurant).to_dict()


@global_exception
@parse_http_event
def get_restaurants(request: Request):
    page_key = request.query_params.get('page_key')
    page_size = request.query_params.get('page_size')

    restaurants, next_page_key = manager.get_restaurants(page_key=page_key, page_size=page_size)

    return PaginatedResponse(
        status_code=200,
        field='restaurants',
        records=restaurants,
        page_key=page_key,
        next_page_key=next_page_key
    ).to_dict()


@global_exception
@parse_http_event
def create_restaurant(request: Request):
    payload = CreateUpdateRestaurantPayloadDTO.from_dict(request.body)
    restaurant = manager.create_restaurant(payload)
    return Response(status_code=200, message_body=restaurant).to_dict()
