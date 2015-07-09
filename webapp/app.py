from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask World!\n'

if __name__ == '__main__':
    app.run('127.0.0.1', debug=True)
