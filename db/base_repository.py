from typing import Generic, TypeVar, Type, Any, Optional, List

from .db_api import BaseModel, DbApi

T = TypeVar('T', bound=BaseModel)


class BaseRepository(Generic[T]):
    def __init__(self, db: DbApi):
        self.db = db

    def get(self, model_class: Type[T], *filters: Any) -> Optional[T]:
        with self.db.session_local(expire_on_commit=False) as session:
            return session.query(model_class) \
                .filter(*filters) \
                .first()

    def get_all(
        self,
        model_class: Type[T],
        page_key: int,
        page_size: int
    ) -> (List[T], Optional[int]):
        with self.db.session_local(expire_on_commit=False) as session:
            offset = (page_key - 1) * page_size
            models = session.query(model_class) \
                .order_by(model_class.created_at) \
                .limit(page_size) \
                .offset(offset) \
                .all()
            total = session.query(model_class).count()

            next_page_key = page_key + 1 if offset + len(models) < total else None
            return models, next_page_key

    def create(self, model: T) -> T:
        with self.db.session_local(expire_on_commit=False) as session:
            session.add(model)
            return model

    def update(self, model: T) -> T:
        with self.db.session_local(expire_on_commit=False) as session:
            return session.merge(model)
