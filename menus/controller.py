from menus.utils.http_events import Request, Response, parse_http_event, global_exception
from .manager import MenusManager
from .dtos import CreateMenuPayloadDTO
from .validators import validate_uuid, validate_positive_int
from .exceptions import InvalidMenuId, InvalidQueryParam


@global_exception
@parse_http_event
def get_menus(request: Request):
    status = request.query_params.get('status', 'ACTIVE')
    page_key = request.query_params.get('page_key')
    page_size = request.query_params.get('page_size', '10')

    if validate_positive_int(page_size):
        raise InvalidQueryParam('page_size', 'Not a positive integer', page_size)

    menus = MenusManager().get_menus(
        status=status,
        page_key=page_key,
        page_size=page_size,
    )
    return Response(status_code=200, message_body=menus).to_dict()


@global_exception
@parse_http_event
def get_menu(request: Request):
    menu_id = request.path_params.get('id')
    if not validate_uuid(menu_id):
        raise InvalidMenuId(menu_id)

    menu = MenusManager().get_menu(menu_id)
    return Response(status_code=200, message_body=menu).to_dict()


@global_exception
@parse_http_event
def create_menu(request: Request):
    payload = CreateMenuPayloadDTO.from_dict(request.body)
    menu = MenusManager().create_menu(payload)
    return Response(status_code=200, message_body=menu).to_dict()
