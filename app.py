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




@socketio.on('json', namespace='/text')
def handle_json(json):
    print('received json: ' + str(json))
    send(json)


@socketio.on('update', namespace='/text')
def handle_json(update):
    print('received json: ' + str(update))
    send(update)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/update", methods=["POST"])
def updated():
    socketio.send("update complete")
    return 




if __name__ == '__main__':
    socketio.run(app)