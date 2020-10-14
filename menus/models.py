from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    UTCDateTimeAttribute,
    NumberAttribute,
    ListAttribute,
    MapAttribute
)
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
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
    description = UnicodeAttribute(null=True)
    price = NumberAttribute(null=True)


class MenusByPrimaryCategoryIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = f'index_by_primary_category_{ENV}'
        host = DYNAMODB_URL
        projection = AllProjection()

    primary_category = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(range_key=True)


class MenusByAreaIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = f'index_by_area_{ENV}'
        host = DYNAMODB_URL
        projection = AllProjection()

    area = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(range_key=True)


class MenusByStatusInxdex(GlobalSecondaryIndex):
    class Meta:
        index_name = f'index_by_status_{ENV}'
        host = DYNAMODB_URL
        projection = AllProjection()

    status = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(range_key=True)


class Menu(Model):
    class Meta:
        table_name = f'menus_{ENV}'
        host = DYNAMODB_URL
        billing_mode = 'PAY_PER_REQUEST'

    id = UnicodeAttribute(hash_key=True, default=str(uuid4()))
    name = UnicodeAttribute(range_key=True)
    primary_category = UnicodeAttribute()
    area = UnicodeAttribute()
    status = UnicodeAttribute()
    description = UnicodeAttribute(null=True)
    address = MenuAddress(null=True)
    items = ListAttribute(of=MenuItem, null=True)
    created_at = UTCDateTimeAttribute(default=datetime.now)
    updated_at = UTCDateTimeAttribute(default=datetime.now)

    index_by_primary_category = MenusByPrimaryCategoryIndex()
    index_by_area = MenusByAreaIndex()
    index_by_status = MenusByStatusInxdex()
