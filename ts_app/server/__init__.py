from flask import Flask
print('hello')
app = Flask(__name__)
print('try')
@app.route('/')
def hello():
    return 'Hello, World'

hello()