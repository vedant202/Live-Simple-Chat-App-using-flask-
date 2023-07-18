from flask import Flask,render_template,request, jsonify, redirect, session
from flask_socketio import SocketIO,emit,join_room,leave_room,send
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

app.debug = True;
Session(app)
socketio = SocketIO(app)
# url_for('static',filename='style.css')
users = []
data = {}

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/send',methods=['POST'])
def handle_post():
    if(request.method =='POST'):
        text = request.get_json()
        print(text)
        return jsonify(text)
    
@app.route('/registerUser',methods=['POST'])
def registerUser():
    if(request.method =='POST'):
        json_data = request.get_json()
        print(json_data)
        session['name'] = json_data['name']
        session['roomId'] = json_data['roomId']
        users.append(data)
        socketio.send('new user joined',session.get('name'),to=json_data['roomId'])
        return {"response":'ok',"user_name":json_data['name']}

@socketio.on('join')
def on_join():
    # session['name'] = data['name']
    # session['roomId'] = data['roomId']
    # print(data)
    join_room(session.get('roomId'))
    emit('new user joined',session.get('name'), to=session.get('roomId'))

@socketio.on('leave')
def on_leave(data):
    username = data['name']
    room = data['roomId']
    leave_room(room)
    emit(username + ' has left the room.', to=room)

# @socketio.on('new user joined')
# def new_user_joined(mess):
#     print(mess)
#     emit('message received',mess,broadcast=True)


@socketio.on('message sent')
def send_message(mess):
    print("Sent message "+mess)
    

    emit('message received',{'mess':mess,'user':session.get('name')}, to=session.get('roomId'))


if __name__=='__main__':
    socketio.run(app, debug=True)
# print(__name__)
