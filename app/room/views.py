# -*- coding: utf8 -*-

from app.models import Room
from app.utils import json_data

from . import room_mod


@room_mod.route('')
def get_rooms():
    rooms = Room.select().order_by(Room.id).dicts()
    import pdb
    pdb.set_trace()
    return json_data(data=rooms)
