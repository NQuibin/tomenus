from uuid import uuid4
from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from db.db_api import BaseModel


class Menu(BaseModel):
    __tablename__ = 'menus'

    id = Column(UUIDType, primary_key=True, default=uuid4)
    restaurant_id = Column(UUIDType, ForeignKey('restaurants.id'))
    name = Column(String(64), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    menu_items = relationship('MenuItem', backref='menu_items', uselist=True, lazy='joined')
