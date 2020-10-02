import json

from functools import wraps
from typing import Callable, Tuple, Dict, Any
from dataclasses import dataclass, is_dataclass, asdict
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Request:
    http_method: str
    headers: Dict[str, Any]
    path_params: Dict[str, Any]
    query_params: Dict[str, Any]
    body: Any


def parse_http_event(func: Callable):
    @wraps(func)
    def wrapper(*args: Tuple[str, Any], **kwargs: Dict[str, Any]):
        event = args[0] if args else kwargs.get('event')

        http_method = event.get('httpMethod')
        headers = event.get('headers')
        path_params = event.get('pathParameters')
        query_params = event.get('queryStringParameters')

        event_body = event.get('body')
        body = None if event_body is None or event_body == '' else json.loads(event_body)

        request = Request(
            http_method=http_method,
            headers=headers,
            path_params=path_params,
            query_params=query_params,
            body=body
        )

        return func(request)

    return wrapper


class Response:
    def __init__(self, access_control: str = '*', status_code: int = 200, message_body: Any = ''):
        self.headers = {
            'Access-Control-Allow-Origin': access_control
        }
        self.status_code = status_code
        self.body = asdict(message_body) if is_dataclass(message_body) else message_body

    def to_dict(self):
        return {
            'headers': self.headers,
            'statusCode': self.status_code,
            'body': json.dumps(self.body if self.body else {})
        }
