from flask import Blueprint, jsonify, request

Tariq = Blueprint("Tariq", __name__, url_prefix="/Trq")

def sum(x, y):
    print(f"You are adding {x} + {y}")
    return x + y

def calculate_sum(Arr :list):
    total_sum = 0
    for num in Arr:
        total_sum += num
    print(f"You are adding elements of the array {Arr}")
    return total_sum

def calculate_average(Arr :list):
    print(f"You are calculating the average of the elements in array {Arr}")
    return (calculate_sum(Arr) / len(Arr))

def print_star(numOfStars):
    star_string = ""
    for _ in range(numOfStars):
        star_string += "*"
    print(f"You are creating {numOfStars} stars")
    return star_string

def ceaser_encrypt(word,k):
    x = []
    for i in word :
        if i.isalpha():
            if i.isupper():
                x.append(chr((ord(i) + k - 65) % 26 + 65))
            else:
                x.append(chr((ord(i) + k - 97) % 26 + 97))
        else:
            x.append(i)
    return ''.join(x)
    

def ceaser_decrypt(word, k):
    return ceaser_encrypt(word,-k)


@Tariq.route("/sum", methods=["GET", "POST"])
def sum_flask():
    if request.method == "GET":
        values = request.args
    elif request.method == "POST":
        values = request.json
    else:
        return jsonify(error="wrong input")

    a = values.get("a")
    b = values.get("b")
    arr = values.get("arr")

    if a is not None and b is not None:
        return jsonify(Answer=sum(int(a), int(b))), 200
    elif arr is not None:
        arr = [int(x) for x in arr.split(",")]  # Convert string elements to integers
        return jsonify(Answer=calculate_sum(arr)), 200
    else:
        return jsonify(error="Missing number or array"), 400

@Tariq.route("/average", methods=["GET", "POST"])   
def average_flask():
    if request.method == "GET":
        values = request.args
    else:
        values = request.json

    arr = values.get("arr")

    if arr is not None:
        arr = [int(x) for x in arr.split(",")]  # Convert string elements to integers
        return jsonify(Answer=calculate_average(arr)), 200
    else:
        return jsonify(error="Missing number or array"), 400

@Tariq.route("/pstar", methods=["GET", "POST"])       
def pstar_flask():
    if request.method == "GET":
        values = request.args
    else:
        values = request.json

    numOfStars = values.get("numOfStars")

    if numOfStars is not None:
        return jsonify(Stars=print_star(int(numOfStars))), 200
    else:
        return jsonify(error="Wrong input"), 400

@Tariq.route("/cencrypt", methods=["GET", "POST"])       
def cencrypt_flask():
    if request.method == "GET":
        values = request.args
    else:
        values = request.json

    word = values.get("sentence")
    k = values.get("key")

    if word is not None and k is not None:
        return jsonify(encrpted=ceaser_encrypt(word,int(k))), 200
    else:
        return jsonify(error="Wrong input"), 400
    
@Tariq.route("/cdecrypt", methods=["GET", "POST"])       
def cdecrypt_flask():
    if request.method == "GET":
        values = request.args
    else:
        values = request.json

    word = values.get("sentence")
    k = values.get("key")

    if word is not None and k is not None:
        return jsonify(decrpted=ceaser_decrypt(word,int(k))), 200
    else:
        return jsonify(error="Wrong input"), 400
