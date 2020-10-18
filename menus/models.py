from uuid import uuid4

from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy_utils import UUIDType

from db.db_api import Base


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(UUIDType, primary_key=True, default=uuid4)
    restaurant_id = Column(UUIDType, ForeignKey('restaurants.id'))
    name = Column(String(64), nullable=False)
    section = Column(String(128), nullable=False)
    section_order = Column(Integer, nullable=False)
    order = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Integer, nullable=True)
