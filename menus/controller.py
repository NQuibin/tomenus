from utils.http_events import (
    Request,
    Response,
    PaginatedResponse,
    parse_http_event,
    global_exception
)
from utils.dict_coder import encode_dict, decode_dict
from .manager import MenusManager
from .dtos import CreateUpdateMenuPayloadDTO
from utils.validators import validate_uuid, validate_positive_int
from .exceptions import InvalidMenuId, InvalidQueryParam


def _validate_menu_id(menu_id: str):
    if not validate_uuid(menu_id):
        raise InvalidMenuId(menu_id)


@global_exception
@parse_http_event
def get_menus(request: Request):
    status = request.query_params.get('status', 'ACTIVE')
    page_key = request.query_params.get('page_key')
    page_size = request.query_params.get('page_size', '10')

    if validate_positive_int(page_size):
        raise InvalidQueryParam('page_size', 'Not a positive integer', page_size)

    menus, next_page_key = MenusManager().get_menus(
        status=status,
        page_key=decode_dict(page_key) if page_key else None,
        page_size=page_size,
    )
    return PaginatedResponse(
        status_code=200,
        records=menus,
        field='menus',
        page_key=page_key,
        next_page_key=encode_dict(next_page_key)
    ).to_dict()


@global_exception
@parse_http_event
def get_menu(request: Request):
    menu_id = request.path_params.get('id')
    _validate_menu_id(menu_id)

    menu = MenusManager().get_menu(menu_id)
    return Response(status_code=200, message_body=menu).to_dict()


@global_exception
@parse_http_event
def create_menu(request: Request):
    payload = CreateUpdateMenuPayloadDTO.from_dict(request.body)
    menu = MenusManager().create_menu(payload)
    return Response(status_code=200, message_body=menu).to_dict()


@global_exception
@parse_http_event
def update_menu(request: Request):
    menu_id = request.path_params.get('id')
    _validate_menu_id(menu_id)

    payload = CreateUpdateMenuPayloadDTO.from_dict(request.body)

    menu = MenusManager().update_menu(menu_id=menu_id, payload=payload)
    return Response(status_code=200, message_body=menu).to_dict()


@global_exception
@parse_http_event
def delete_menu(_: Request):
    return Response(status_code=501, message_body='Not implemented').to_dict()
