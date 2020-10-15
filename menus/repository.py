from typing import List, Optional, Tuple
from .models import Menu
from pynamodb.pagination import ResultIterator


class MenusRepository:
    def __init__(self):
        self.model = Menu

    def _query_raw(self, hash_key: str, **kwargs) -> ResultIterator:
        return self.model.query(hash_key, **kwargs)

    def _query(self, hash_key: str, **kwargs) -> List[Menu]:
        results = self._query_raw(hash_key, **kwargs)
        return [result for result in results]

    def get(self, hash_key: str) -> Optional[Menu]:
        results = self._query(hash_key)
        return results[0] if len(results) else None

    def get_all(
        self,
        status: str,
        page_key: str,
        page_size: str,
        is_ascending: bool = True
    ) -> Tuple[List[Menu], dict]:
        results = self._query_raw(
            hash_key=status,
            limit=int(page_size),
            scan_index_forward=is_ascending,
            last_evaluated_key=page_key,
            index_name=self.model.index_by_status.Meta.index_name
        )
        return [result for result in results], results.last_evaluated_key

    def create(self, model: Menu) -> Menu:
        model.save()
        return model
