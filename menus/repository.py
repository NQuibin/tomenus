from .models import Menu


class MenusRepository:
    def __init__(self):
        self.model = Menu

    def find(self, hash_key: str):
        query_results = self.model.query(hash_key)
        results = [result for result in query_results]
        return results[0] if len(results) else None
