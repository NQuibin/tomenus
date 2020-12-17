from os import getenv

from mongoengine import connect, signals

from .signals import update_updated_at

db_connection = None

signals.pre_save.connect(update_updated_at)


def establish_connection():
    global db_connection
    if db_connection is None:
        host = getenv('DB_HOST', 'localhost')
        port = getenv('DB_PORT', '27017')
        db_name = getenv('DB_NAME', 'tomenusdev')
        db_username = getenv('DB_USERNAME', 'tomenus')
        db_password = getenv('DB_PASSWORD', 'tomenus123123')

        db_connection = connect(
            host=f'mongodb://{db_username}:{db_password}@{host}:{port}/{db_name}?authSource=admin'
        )
