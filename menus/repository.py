from db.db_api import DbApi
from .models import Menu


class MenuRepository:
    def __init__(self):
        self.db = DbApi()

    def get_menu(self, menu_id: str) -> Menu:
        with self.db.session_local(expire_on_commit=False) as session:
            return session.query(Menu) \
                .filter(Menu.id == menu_id) \
                .first()
