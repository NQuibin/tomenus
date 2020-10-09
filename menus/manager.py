from .repository import MenusRepository
from .dtos import MenuDTO
from .utils import create_menu_dto_from_model


class MenusManager:
    def __init__(self):
        self.repository = MenusRepository()

    def get_menu(self, menu_id: str) -> MenuDTO:
        menu = self.repository.find(menu_id)
        return create_menu_dto_from_model(menu)
