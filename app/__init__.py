from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    from .room import room_mod
    app.register_blueprint(room_mod, url_prefix='/rooms')
    return app
