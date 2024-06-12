from flask import Flask, request, jsonify
from blueprints.ridhwan import ridhwan
from blueprints.sara import sara

app = Flask("Testing app")
app.register_blueprint(ridhwan)

def sum(a: int, b: int):
    print(f"You are going to add {a} + {b} together!!!!!!!")
    return a + b

@app.route("/sum", methods=["GET", "POST"])
def sum_flask():
    if request.method == "GET":
        values = request.args
    elif request.method == "POST":
        values = request.json
    else:
        return jsonify(error="Invalid method!"), 405
    
    a = values.get("a")
    b = values.get("b")
    if a is None:
        return jsonify(error="Missing `a`"), 400
    if b is None:
        return jsonify(error="Missing `b`"), 400

    return jsonify(answer= sum(int(a), int(b))), 200


if __name__ == "__main__":
    app.run()