from typing import List, Optional

from db import DbApi, BaseRepository
from .models import MenuItem


class MenuItemRepository(BaseRepository):
    def __init__(self):
        super().__init__(DbApi())

    def get_menu_item(self, menu_item_id: str) -> MenuItem:
        return self.get(MenuItem, MenuItem.id == menu_item_id)

    def get_menu_items(
            self,
            page_key: int,
            page_size: int
    ) -> (List[MenuItem], Optional[str]):
        return self.get_all(model_class=MenuItem, page_key=page_key, page_size=page_size)

    def create_menu_item(self, model: MenuItem) -> MenuItem:
        return self.create(model)

    def update_menu_item(self, model: MenuItem) -> MenuItem:
        return self.update(model)
