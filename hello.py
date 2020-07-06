from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login')
def login():
    return 'login'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

@app.route('/projects/')
def projects():
    return 'The project page'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))