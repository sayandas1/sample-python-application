# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is the green version of the app.'

if __name__ == '__main__':
    app.run(debug=True)
