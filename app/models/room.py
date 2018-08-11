
from peewee import CharField, DateTimeField

from . import BaseModel


class Room(BaseModel):
    name = CharField(unique=True)
    create_time = DateTimeField()
