import RPi.GPIO as GPIO
import json
import os

from flask import Flask
from flask import request
from flask import make_response


app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  # Use board pin numbering
GPIO.setup(16, GPIO.OUT)  # Setup GPIO Pin to OUTPUT


@app.route('/on', methods=['GET'])
def makeon():
    req = request.get_json(silent=True, force=True)

    GPIO.output(16, True)  # State is true/false
    return "turning on"



@app.route('/off', methods=['GET'])
def makeoff():
    req = request.get_json(silent=True, force=True)

    GPIO.output(16, False)  # State is true/false   
    return "turning on"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
