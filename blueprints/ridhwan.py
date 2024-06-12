from flask import Blueprint, jsonify

ridhwan = Blueprint("ridhwan", __name__, url_prefix="/rid")

@ridhwan.get("/hello")
def hello_fn():
    return jsonify(message="Hello!")
