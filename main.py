#
#   Author: Onur Sedef
#   Project Name: Chat App w/ Flask, Socket.io
#   Credit: youtube/NeuralNine
#

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET'] = "secret123"
socketio = SocketIO(app, cors_allowed_origin="*")

@socketio.on('message')
def handle_message(message):
    print('Received message: {0}'.format(message))
    if message != "User connected!":
        send(message, broadcast=True)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host="localhost")