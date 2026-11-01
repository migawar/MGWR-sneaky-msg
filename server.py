from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mgwr-leerkracht-fopper'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('msg')
def handle_message(data):
    # Ontvang het MGWR-bericht en stuur het direct door naar iedereen
    username = data.get('username', 'Anoniem')
    message = data.get('message', '')
    emit('receive_msg', {'username': username, 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)