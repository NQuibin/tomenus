from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, Text, Integer, DateTime, ForeignKey
from sqlalchemy_utils import UUIDType

from db.db_api import Base


class MenuItem(Base):
    __tablename__ = 'menu_items'

    id = Column(UUIDType, primary_key=True, default=uuid4)
    menu_id = Column(UUIDType, ForeignKey('menus.id'))
    name = Column(String(64), nullable=False)
    section = Column(String(128), nullable=False)
    section_order = Column(Integer, nullable=False)
    order = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
