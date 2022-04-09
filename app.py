import flask
from flask import *
from flask_cors import CORS

from src import datetimeService

app = Flask(__name__)
CORS(app)


@app.route(f'/api/v1/timestamp', methods=['GET'])
def getTimestamp():
    return flask.jsonify({
        "timestamp": datetimeService.getTimestamp()
    })
