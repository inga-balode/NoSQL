import redis
from flask import Flask
from flask import request
from time import strftime

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def theanswer():
    visits = dict()
    new = 0
    user = request.remote_addr
    day = strftime("%Y-%m-%d")
    if user not in visits.values():
        new += 1
        if day in visits.keys():
            visits[day].append(user)
        else:
            visits[day] = user
    r.hmset("visit_dict", visits)
    return f'new visitors: {new} all visitors: {visits}'


