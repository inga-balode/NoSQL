import redis
from flask import Flask
from flask import request

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def theanswer():
    visits = []
    new = 0
    user = request.remote_addr
    if user not in visits:
        new += 1
        visits.append(user)
    return f'new visitors: {new} all visitors: {visits}'


