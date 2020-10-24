from typing import Dict, Any

from utils.http_events import (
    Request,
    Response,
    PaginatedResponse,
    parse_http_event,
    global_exception
)
from utils.validators import validate_uuid
from .exceptions import InvalidMenuItemId
from .manager import MenuItemManager
from .dtos import CreateUpdateMenuItemPayloadDTO

manager = MenuItemManager()


@global_exception
@parse_http_event
def get_menu_item(request: Request) -> Dict[str, Any]:
    menu_item_id = request.path_params.get('menu_item_id')
    if not validate_uuid(menu_item_id):
        raise InvalidMenuItemId(menu_item_id)

    menu_item = manager.get_menu_item(menu_item_id)
    return Response(status_code=200, message_body=menu_item).to_dict()


@global_exception
@parse_http_event
def get_menu_items(request: Request) -> Dict[str, Any]:
    page_key = request.query_params.get('page_key', '1')
    page_size = request.query_params.get('page_size', '10')

    menu_items, next_page_key = manager.get_menu_items(
        page_key=page_key,
        page_size=page_size
    )
    return PaginatedResponse(
        status_code=200,
        field='menus_items',
        records=menu_items,
        page_key=page_key,
        next_page_key=next_page_key
    ).to_dict()


@global_exception
@parse_http_event
def create_menu_item(request: Request) -> Dict[str, Any]:
    payload = CreateUpdateMenuItemPayloadDTO.from_dict(request.body)
    menu_item = manager.create_menu_item(payload)
    return Response(status_code=200, message_body=menu_item).to_dict()


@global_exception
@parse_http_event
def update_menu_item(request: Request) -> Dict[str, Any]:
    menu_item_id = request.path_params.get('menu_item_id')
    if not validate_uuid(menu_item_id):
        raise InvalidMenuItemId(menu_item_id)

    payload = CreateUpdateMenuItemPayloadDTO.from_dict(request.body)

    menu_item = manager.update_menu_item(menu_item_id=menu_item_id, payload=payload)
    return Response(status_code=200, message_body=menu_item).to_dict()
