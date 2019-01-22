import os

from flask import Flask


app = Flask(__name__)

@app.route('/message')
def message():
    return '{}'.format(os.getenv('MY_SECRET_MESSAGE'))

app.run(host='0.0.0.0')
