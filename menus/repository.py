from typing import List, Optional
from .models import Menu


class MenusRepository:
    def __init__(self):
        self.model = Menu

    def _query(self, hash_key: str) -> List[Menu]:
        results = self.model.query(hash_key)
        return [result for result in results]

    def _scan(self) -> List[Menu]:
        results = self.model.scan()
        return [result for result in results]

    def get(self, hash_key: str) -> Optional[Menu]:
        results = self._query(hash_key)
        return results[0] if len(results) else None

    def get_all(self) -> List[Menu]:
        return self._scan()

    def create(self, model: Menu) -> Menu:
        model.save()
        return model
