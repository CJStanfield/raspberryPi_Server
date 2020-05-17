from flask import request
from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pinList = [7,8]
for i in pinList:
    GPIO.setup(i, GPIO.OUT)

app = Flask(__name__)


@app.route('/', methods=["GET"])
def api_root():
    return {
        "relay_url": request.url + "relay/{0 | 1}",
    }


@app.route('/relay/fan', methods=["GET"])
def toggle_relay_fan():
    state = int(request.args.get('state'))
    GPIO.output(pinList[0], state)
    return {"message": "Fan relay set to value: " + request.args.get('state')}

@app.route('/relay/fridge', methods=["GET"])
def toggle_relay_fridge():
    state = int(request.args.get('state'))
    GPIO.output(pinList[1], state)
    return {"message": "Fridge relay set to value: " + request.args.get('state')}

@app.route('/relay/cleanup', methods=["GET"])
def gpio_cleanup():
    GPIO.cleanup()
    return {"message": "GPIO pins cleared"}


if __name__ == "__main__":
    app.run()
