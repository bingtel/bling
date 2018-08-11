
from flask_socketio import SocketIO

from app import create_app

app = create_app()
sapp = SocketIO(app)

if __name__ == '__main__':
    sapp.run(app, host='0.0.0.0')
