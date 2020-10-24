from typing import List, Optional

from db import DbApi, BaseRepository
from .models import Menu


class MenuRepository(BaseRepository):
    def __init__(self):
        super().__init__(DbApi())
