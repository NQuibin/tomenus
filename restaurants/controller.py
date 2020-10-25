from typing import Dict, Any

from shared.http_events import (
    Request,
    Response,
    PaginatedResponse,
    parse_http_event,
    global_exception
)
from shared.validators import validate_uuid
from .manager import RestaurantManager
from .exceptions import InvalidRestaurantId
from .dtos import CreateUpdateRestaurantPayloadDTO

manager = RestaurantManager()


@global_exception
@parse_http_event
def get_restaurant(request: Request):
    restaurant_id = request.path_params.get('restaurant_id')
    if not validate_uuid(restaurant_id):
        raise InvalidRestaurantId(restaurant_id)

    full = request.query_params.get('full', 'false')

    restaurant = manager.get_restaurant(
        restaurant_id=restaurant_id,
        full=full.lower() == 'true'
    )
    return Response(status_code=200, message_body=restaurant).to_dict()


@global_exception
@parse_http_event
def get_restaurants(request: Request) -> Dict[str, Any]:
    page_key = request.query_params.get('page_key', '1')
    page_size = request.query_params.get('page_size', '10')
    full = request.query_params.get('full', 'false')

    restaurants, next_page_key = manager.get_restaurants(
        page_key=page_key,
        page_size=page_size,
        full=full.lower() == 'true'
    )
    return PaginatedResponse(
        status_code=200,
        field='restaurants',
        records=restaurants,
        page_key=page_key,
        next_page_key=next_page_key
    ).to_dict()


@global_exception
@parse_http_event
def create_restaurant(request: Request) -> Dict[str, Any]:
    payload = CreateUpdateRestaurantPayloadDTO.from_dict(request.body)
    restaurant = manager.create_restaurant(payload)
    return Response(status_code=200, message_body=restaurant).to_dict()


@global_exception
@parse_http_event
def update_restaurant(request: Request) -> Dict[str, Any]:
    restaurant_id = request.path_params.get('restaurant_id')
    if not validate_uuid(restaurant_id):
        raise InvalidRestaurantId(restaurant_id)

    payload = CreateUpdateRestaurantPayloadDTO.from_dict(request.body)

    restaurant = manager.update_restaurant(restaurant_id=restaurant_id, payload=payload)
    return Response(status_code=200, message_body=restaurant).to_dict()
