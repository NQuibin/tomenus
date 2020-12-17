from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, ReferenceField


class Address(Document):
    address1 = StringField(required=True)
    address2 = StringField(max_length=64)
    city = StringField(required=True, max_length=64)
    province = StringField(required=True, max_length=64)
    code = StringField(required=True, max_length=16)
    country = StringField(required=True, max_length=64)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)


class Restaurant(Document):
    name = StringField(required=True)
    primary_category = StringField(required=True)
    status = StringField(required=True)
    description = StringField()
    address = ReferenceField(Address, db_field='address_id')
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
