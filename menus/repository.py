from typing import List, Optional

from db import DbApi, BaseRepository
from .models import Menu


class MenuRepository(BaseRepository):
    def __init__(self):
        super().__init__(DbApi())

    def get_menu(self, menu_id: str) -> Menu:
        return self.get(Menu, Menu.id == menu_id)

    def get_menus(
            self,
            page_key: int,
            page_size: int
    ) -> (List[Menu], Optional[str]):
        return self.get_all(model_class=Menu, page_key=page_key, page_size=page_size)

    def create_menu(self, model: Menu) -> Menu:
        return self.create(model)

    def update_menu(self, model: Menu) -> Menu:
        return self.update(model)
