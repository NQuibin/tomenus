from utils.http_events import (
    Request,
    Response,
    parse_http_event,
    global_exception
)
from utils.validators import validate_uuid
from .manager import RestaurantManager
from .exceptions import InvalidRestaurantId


@global_exception
@parse_http_event
def get_restaurant(request: Request):
    restaurant_id = request.path_params.get('id')
    if not validate_uuid(restaurant_id):
        raise InvalidRestaurantId(restaurant_id)

    restaurant = RestaurantManager().get_restaurant(restaurant_id)
    return Response(status_code=501, message_body=restaurant).to_dict()
