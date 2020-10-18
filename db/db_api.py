import os

from contextlib import contextmanager
from typing import Any, Iterator

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool

meta = MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "%(table_name)s_pkey"
})

Base = declarative_base(metadata=meta)


def get_database_url(db_dialect: str = None, db_user: str = None, db_password: str = None, db_host: str = None, db_name: str = None, db_port: str = None) -> str:
    db_dialect = db_dialect or os.getenv('DB_DIALECT', 'postgresql')
    db_user = db_user or os.getenv('DB_USERNAME')
    db_password = db_password or os.getenv('DB_PASSWORD')
    db_host = db_host or os.getenv('DB_HOST')
    db_name = db_name or os.getenv('DB_NAME')
    db_port = db_port or os.getenv('DB_PORT', '5432')
    assert db_user is not None and db_password is not None and db_host is not None and db_name is not None
    db_url = f'{db_dialect}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    return db_url


class DbApi:
    def __init__(self, db_url: str = get_database_url()):
        self.engine = create_engine(db_url, poolclass=NullPool)
        self.session_factory = sessionmaker(bind=self.engine)

    @contextmanager
    def session_local(self, *args: Any, **kwargs: Any) -> Iterator[Session]:
        session = self.session_factory(*args, **kwargs)
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
