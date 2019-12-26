from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('my event', namespace='/test')
def handle_my_custom_namespace_event(json):
    print('test: received json: ' + str(json))

    # TODO: database query +++++
    
    send("hello, world")


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app)