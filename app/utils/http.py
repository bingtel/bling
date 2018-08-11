# -*- coding: utf-8 -*-

from flask import jsonify


class _Json(dict):
    def __init__(self, code, msg, data):
        super(_Json, self).__init__(
            code=code, msg=msg, data=data)

    def __call__(self):
        return jsonify({
            'code': self['code'],
            'msg': self['msg'],
            'data': self['data'],
        })


def json_data(code=200, msg='', data=None):
    return _Json(code, msg, data)()
