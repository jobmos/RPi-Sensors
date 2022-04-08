from flask import Flask, jsonify
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

app = Flask(__name__)

@app.route("/")
def get():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    response = {
        "temperature": temperature,
        "humidity": humidity
    }

    return response

if __name__ == "__main__":
    app.run(debug=True)
