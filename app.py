from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/chat", methods=["GET"])
def chat_page():
   return render_template("index.html")
    
@socketio.on('message')
def handle_connection(msg):
   emit('message', msg, broadast=True)
    
if __name__ == "__main__":
    socketio.run(app, debug=True)