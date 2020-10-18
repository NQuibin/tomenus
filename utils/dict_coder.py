import json
import base64


def encode_dict(a_dict: dict):
    json_str = json.dumps(a_dict)
    json_str_bytes = json_str.encode('ascii')
    b64_bytes = base64.b64encode(json_str_bytes)
    return b64_bytes.decode('ascii')


def decode_dict(base64_str: str):
    b64_bytes = base64_str.encode('ascii')
    json_str_bytes = base64.b64decode(b64_bytes)
    json_str = json_str_bytes.decode('ascii')
    return json.loads(json_str)
