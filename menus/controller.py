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
from .dtos import CreateUpdateMenuPayloadDTO

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
def get_menus(request: Request) -> Dict[str, Any]:
    page_key = request.query_params.get('page_key', '1')
    page_size = request.query_params.get('page_size', '10')
    full = request.query_params.get('full', 'false')

    menus, next_page_key = manager.get_menus(
        page_key=page_key,
        page_size=page_size,
        full=full.lower() == 'true'
    )
    return PaginatedResponse(
        status_code=200,
        field='menus',
        records=menus,
        page_key=page_key,
        next_page_key=next_page_key
    ).to_dict()


@global_exception
@parse_http_event
def create_menu(request: Request) -> Dict[str, Any]:
    payload = CreateUpdateMenuPayloadDTO.from_dict(request.body)
    menu = manager.create_menu(payload)
    return Response(status_code=200, message_body=menu).to_dict()


@global_exception
@parse_http_event
def update_menu(request: Request) -> Dict[str, Any]:
    menu_id = request.path_params.get('menu_id')
    if not validate_uuid(menu_id):
        raise InvalidMenuId(menu_id)

    payload = CreateUpdateMenuPayloadDTO.from_dict(request.body)

    menu = manager.update_menu(menu_id=menu_id, payload=payload)
    return Response(status_code=200, message_body=menu).to_dict()
