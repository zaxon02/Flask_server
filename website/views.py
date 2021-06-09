from flask import Blueprint
from flask import request, render_template
from flask_login import login_required, current_user
import datetime


views = Blueprint('views', __name__)

MESSAGES = {}

@views.route('/')
@login_required
def home():
    ip = request.remote_addr
    cmd = request.args.get('cmd')
    result = get_result(cmd, ip)

    client = request.args.get('device')

    if client not in MESSAGES:
        MESSAGES[client] = []
    if cmd != 'getmsgs':
        MESSAGES[client].append(result)

    if cmd == 'getmsgs':
        return render_template('index.html', messages=result, user=current_user)
    return render_template('index.html', result=result, user=current_user)


def get_result(cmd, ip):
    if cmd == 'getmsgs':
        return MESSAGES[ip]
    if cmd == 'time':
        return str(datetime.datetime.now().time())

