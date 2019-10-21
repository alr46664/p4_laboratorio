#!/usr/bin/python
import sys
from flask import Flask
app = Flask(__name__)

if len(sys.argv) < 2:
    port = 8888 
else:
    port = sys.argv[1]

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)