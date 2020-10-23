from typing import Dict, Any

from utils.http_events import (
    Request,
    Response,
    PaginatedResponse,
    parse_http_event,
    global_exception
)
from utils.validators import validate_uuid
from .exceptions import InvalidMenuId
from .manager import MenuManager

manager = MenuManager()


@global_exception
@parse_http_event
def get_menu(request: Request) -> Dict[str, Any]:
    menu_id = request.path_params.get('menu_id')
    if not validate_uuid(menu_id):
        raise InvalidMenuId(menu_id)

    full = request.query_params.get('full', 'false')

    menu = MenuManager().get_menu(menu_id=menu_id, full=full.lower() == 'true')
    return Response(status_code=200, message_body=menu).to_dict()


@global_exception
@parse_http_event
def get_menus(_: Request) -> Dict[str, Any]:
    return Response(status_code=501, message_body='Not implemented').to_dict()


@global_exception
@parse_http_event
def create_menu(_: Request) -> Dict[str, Any]:
    return Response(status_code=501, message_body='Not implemented').to_dict()
