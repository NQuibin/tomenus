from .http_utils import Request, Response, parse_http_event
from .manager import MenusManager
from .validators import validate_uuid


@parse_http_event
def get_menus(_: Request):
    return Response(status_code=501, message_body='Not implemented').to_dict()


@parse_http_event
def get_menu(request: Request):
    menu_id = request.path_params.get('id')
    if not validate_uuid(menu_id):
        return Response(status_code=400, message_body='Invalid menu id').to_dict()

    menu = MenusManager().get_menu(menu_id)
    return Response(status_code=200, message_body=menu).to_dict()
