from typing import Any


class HttpEventHandlerException(Exception):
    def __init__(self, status_code: int, message: Any):
        super().__init__(str(message))
        self.statusCode = status_code
        self.message = message
