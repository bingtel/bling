# -*- coding: utf8 -*-

from flask import Blueprint

room_mod = Blueprint('room', __name__)

from . import views
