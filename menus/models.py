from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    UTCDateTimeAttribute,
    NumberAttribute,
    ListAttribute,
    MapAttribute
)
from pynamodb.indexes import LocalSecondaryIndex, AllProjection
from uuid import uuid4
from datetime import datetime

from menus import ENV, DYNAMODB_URL


class MenuAddress(MapAttribute):
    address1 = UnicodeAttribute()
    address2 = UnicodeAttribute(null=True)
    city = UnicodeAttribute()
    province = UnicodeAttribute()
    postal_code = UnicodeAttribute()
    country = UnicodeAttribute()


class MenuItem(MapAttribute):
    id = UnicodeAttribute(default=str(uuid4()))
    name = UnicodeAttribute()
    price = NumberAttribute(default=0)


class MenusByPrimaryCategoryIndex(LocalSecondaryIndex):
    class Meta:
        index_name = f'index_by_primary_category_{ENV}'
        host = DYNAMODB_URL
        projection = AllProjection()

    id = UnicodeAttribute(hash_key=True, default=str(uuid4()))
    primary_category = UnicodeAttribute(range_key=True)


class MenusByAreaIndex(LocalSecondaryIndex):
    class Meta:
        index_name = f'index_by_area_{ENV}'
        host = DYNAMODB_URL
        projection = AllProjection()

    id = UnicodeAttribute(hash_key=True, default=str(uuid4()))
    area = UnicodeAttribute(range_key=True)


class Menu(Model):
    class Meta:
        table_name = f'menus_{ENV}'
        host = DYNAMODB_URL

    id = UnicodeAttribute(hash_key=True, default=str(uuid4()))
    name = UnicodeAttribute(range_key=True)
    primary_category = UnicodeAttribute()
    area = UnicodeAttribute()
    address = MenuAddress(null=True)
    items = ListAttribute(of=MenuItem, null=True)
    created_at = UTCDateTimeAttribute(default=datetime.now)
    updated_at = UTCDateTimeAttribute(default=datetime.now)

    index_by_primary_category = MenusByPrimaryCategoryIndex()
    index_by_area = MenusByAreaIndex()
