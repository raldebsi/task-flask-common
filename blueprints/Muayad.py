from flask import Blueprint, jsonify, request

muayad = Blueprint("muayad", __name__, url_prefix="/mw")

def Sum(my_list: list):
    total_sum = sum(my_list)
    print(f"You are going to add the array {my_list} together!!!!!!!")
    return total_sum

@muayad.route("/sum", methods=["GET","POST"])
def sum_flask():
    if request.method == "GET":
        values = request.args
    else:
        values = request.json

    my_list = values.get("my_list")
    if my_list is None:
        return jsonify(error="Missing 'my_list' parameter"), 400
    my_list = [int(num) for num in my_list.split(',')]
    return jsonify(answer=Sum(my_list)), 200


def CalculateAvg(my_list):
    avg = 0
    sum = 0
    for num in my_list:
        sum += num

    avg = sum/len(my_list)
    return avg  


@muayad.route("/avg", methods=["GET","POST"])
def avg_flask():
    if request.method == "GET":
        values = request.args
    else:
        values = request.json

    my_list = values.get("my_list")
    if my_list is None:
        return jsonify(error="Missing 'my_list' parameter"), 400
    my_list = [int(num) for num in my_list.split(',')]
    return jsonify(answer=CalculateAvg(my_list)), 200


def PrintStars(x):
    return "*" * x

@muayad.route("/stars", methods=["GET", "POST"])
def stars_flask():
    if request.method == "GET":
        values = request.args
    elif request.method == "POST":
        values = request.json
    else:
        return jsonify(error="Invalid Method"), 405

    x = values.get("x")
    if x is None:
        return jsonify(error="Missing 'num' parameter"), 400
    return jsonify(answer=PrintStars(int(x))), 200


def Cypher(Sentence, Key):
    cipher = ""
    for char in Sentence:
        if char.isupper():
            shifted = (ord(char) + Key - ord('A')) % 26 + ord('A')
        elif char.islower():
            shifted = (ord(char) + Key - ord('a')) % 26 + ord('a')
        else:
            shifted = ord(char)

        cipher += chr(shifted)

    return cipher

def UnCypher(Sentence, Key):
    return Cypher(Sentence, -Key)

@muayad.route("/cyp", methods=["GET", "POST"])
def cypher_flask():
    if request.method == "GET":
        values = request.args
    else:
        values = request.json
        
    Sentence = values.get("Sentence")
    Key = values.get("Key")

    if Sentence is None:
        return jsonify(error="Missing 'Sentence' parameter"), 400
    if Key is None:
        return jsonify(error="Missing 'Key' paramenter"), 400
    return jsonify(answer=Cypher(Sentence,int(Key))), 200

@muayad.route("/uncyp", methods=["GET", "POST"])
def uncypher_flask():
    if request.method == "GET":
        values = request.args
    else:
        values = request.json
        
    Sentence = values.get("Sentence")
    Key = values.get("Key")

    if Sentence is None:
        return jsonify(error="Missing 'Sentence' parameter"), 400
    if Key is None:
        return jsonify(error="Missing 'Key' paramenter"), 400
    return jsonify(answer=UnCypher(Sentence,int(Key))), 200


    