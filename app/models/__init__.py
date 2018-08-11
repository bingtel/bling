# -*- coding: utf-8 -*-

from peewee import (
    SqliteDatabase,
    Model,
)


db = SqliteDatabase('db.db')


class BaseModel(Model):
    class Meta:
        database = db

from .room import Room
