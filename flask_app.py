from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

wines = [
    {"id": 1, "alcohol": 8, "quality": 10},
    {"id": 2, "alcohol": 12, "quality": 8},
    {"id": 3, "alcohol": 10.5, "quality": 9},
]


@app.route("/")
def hello_world():
    return "<p>Hello, from TechLabs!</p>"


@app.route("/api/wines/all", methods=["GET"])
def return_all():
    return jsonify(wines)