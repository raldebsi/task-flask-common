from flask import Blueprint, jsonify,request



ranim = Blueprint("ranim", __name__, url_prefix="/ran")
    
def sum(n1,n2):
    return n1+n2

@ranim.route("/sum", methods=["GET", "POST"])
def sum_flask():
    if request.method == "GET":
        values =request.args
    elif request.method == "POST":
        values =request.json
    else:
        return jsonify(error="Invalid method!"), 405
    
    n1 = values.get("n1")
    n2 = values.get("n2")
    if n1 is None:

        return jsonify(error="Missing `n1`"), 400
    
    if n2 is None:
        return jsonify(error="Missing `n2`"), 400
    
    
    return jsonify(
        answer= sum(
            int(n1), int(n2)
            )
        ), 200

def average_calculate(n1,n2):
    return n1+n2/2
    

@ranim.route("/average", methods=["GET", "POST"])
def average_flask():
     if request.method == "GET":
        values= request.args
     elif request.method == "POST":
        values= request.json
     else:
        return jsonify(error="Invalid method!"), 405
     
     n1 = values.get("n1")
     n2 = values.get("n2")
     if n1 is None:

        return jsonify(error="Missing `n1`"), 400
     
     if n2 is None:
        return jsonify(error="Missing `n2`"), 400
     
     return jsonify(
         answer = average_calculate(
             int(n1), int(n2)
            )
         ), 200


def print_stars(nS):

    stars=""
    for i in range(nS):
        stars=stars+"*"
    return "Your stars: "+stars

@ranim.route("/prints", methods=["GET", "POST"])
def print_stars_flask():

    if request.method == "GET":
         values = request.args
    elif request.method == "POST":
        values = request.json
    else:
        return jsonify(error="Invalid method!"), 405
    
    stars = values.get("stars")
    
    if stars is None or not str(stars).isdigit() :
        return jsonify(error="Missing number of stars"), 400
    if not str(stars).isdigit() or str(stars).isdigit()<0:
        return jsonify(error="Invalid stars number"), 400
    
    return jsonify(
        answer= print_stars(
            int(stars)
            )
        ), 200


def caeser_do(k,msg):
   
    new= ''.join([chr(((ord(i) - ord('a') + k) % 26) + ord('a')) for i in msg])
    return new

def caeser_undo(k,msg):
    
    new=''.join([chr((ord(i) - k - ord('a')) % 26 + ord('a')) for i in msg])
    return new

@ranim.route("/caeserdo", methods=["GET", "POST"])
def caeser_do_flask():

    if request.method == "GET":
         values = request.args
    elif request.method == "POST":
        values = request.json
    else:
        return jsonify(error="Invalid method!"), 405
    
    shiftNumber = values.get("shiftNumber")
    message=values.get("msg")

    if shiftNumber is None:
        return jsonify(error="Missing `shiftNumber`"), 400
    
    if not str(shiftNumber).isdigit():
        return jsonify(error="Invalid shift number"), 400
    return jsonify(
        answer= caeser_do(
            int(shiftNumber), message
            )
            ), 200

@ranim.route("/caeserundo", methods=["GET", "POST"])
def caeser_undo_flask():

    if request.method == "GET":
         values = request.args
    elif request.method == "POST":
        values = request.json
    else:
        return jsonify(error="Invalid method!"), 405
    
    shiftNumber = values.get("shiftNumber")
    message=values.get("msg")
    if shiftNumber is None :
        return jsonify(error="Missing `shiftNumber`"), 400

    if not str(shiftNumber).isdigit():
        return jsonify(error="Invalid shift number"), 400
    
    return jsonify(
        answer= caeser_undo(
            int(shiftNumber),message
            )
        ), 200