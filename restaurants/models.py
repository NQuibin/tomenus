from uuid import uuid4
from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from db.db_api import Base
from menus.models import Menu


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(UUIDType, primary_key=True, default=uuid4)
    name = Column(String(128), nullable=False)
    primary_category = Column(String(128), nullable=False)
    area = Column(String(64), nullable=False)
    description = Column(Text, nullable=True)
    address1 = Column(String(128), nullable=True)
    address2 = Column(String(28), nullable=True)
    city = Column(String(128), nullable=True)
    province = Column(String(64), nullable=True)
    postal_code = Column(String(16), nullable=True)
    country = Column(String(64), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    menus = relationship(Menu, backref='menus', uselist=True, lazy='joined')
