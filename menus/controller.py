from .http_utils import Request, Response, parse_http_event, global_exception
from .manager import MenusManager
from .validators import validate_uuid
from .exceptions import InvalidMenuId


@global_exception
@parse_http_event
def get_menus(_: Request):
    menus = MenusManager().get_menus()
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
def add_menu(_: Request):
    return Response(status_code=500, message_body='Not implemented').to_dict()
