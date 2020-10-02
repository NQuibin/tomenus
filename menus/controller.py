from .http_utils import Request, Response, parse_http_event


@parse_http_event
def get_menus(_: Request):
    return Response(status_code=501, message_body='Not implemented').to_dict()
