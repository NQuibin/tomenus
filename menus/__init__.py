from os import getenv

ENV = getenv('ENV', 'dev')
DYNAMODB_URL = None

if getenv('USE_DYNAMODB_LOCAL', 'false') == 'true':
    DYNAMODB_URL = 'http://localhost:8000'
