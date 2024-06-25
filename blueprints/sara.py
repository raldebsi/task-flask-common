from flask import Blueprint, request, jsonify

sara= Blueprint("sara", __name__, url_prefix="/sara")

def calculate_sum(x,y):
    return x+y

def calculate_avg(x,y):
    return calculate_sum(x,y)/2

def print_stars(n):
    return "*"*n


def caeser_mod(word,k):
    return "".join([ chr((ord(i) - ord("a") + k ) %26 + ord("a")) for i in word])
    
def caeser_unmod(word,k):
    return "".join([ chr((ord(i) - k -  ord("a")) %26 + ord("a"))  for i in word])
    
@sara.route("/sum", methods= ["GET", "POST"])
def sum_flask():
    if request.method== "GET":
        vals= request.args
    elif request.method== "POST":
        vals= request.json
    else:
        return jsonify(error="Invalid method!"), 405 
    
    x= vals.get("x")
    y= vals.get("y")
    
    if x is None:
        return jsonify(error= "x is missing"), 400
    if y is None:
        return jsonify(error= "y is missing"), 400
    
    return jsonify( answer= calculate_sum(int(x),int(y))), 200


@sara.route("/avg", methods= ["GET", "POST"])
def avg_flask():
    if request.method== "GET":
        vals= request.args
    elif request.method=="POST":
        vals= request.json
        
    else:
        return jsonify(error="Invalid method!"), 405 
    
    x= vals.get("x")
    y= vals.get("y")
    
    if x is None:
        return jsonify(error= "x is missing"), 400
    if y is None:
        return jsonify(error= "y is missing"), 400
    
    return jsonify( answer= calculate_avg(int(x),int(y))), 200


@sara.route("/stars", methods= ["GET", "POST"])
def stars_flask():
    if request.method== "GET":
        vals= request.args
    elif request.method=="POST":
        vals= request.json
    else:
        return jsonify(error="Invalid method!"), 405 
    
    n= vals.get("n")
    if n is None:
        return jsonify(error= "n is missing"), 400
    
    return jsonify( answer= print_stars(int(n)) ), 200


@sara.route("/caeser", methods= ["GET", "POST"])
def caeser_flask():
    if request.method== "GET":
        vals= request.args
    elif request.method=="POST":
        vals= request.json
    else:
        return jsonify(error="Invalid method!"), 405 
    
    word= vals.get("word")
    k= vals.get("k")
    
    if word is None:
        return jsonify(error= "word is missing"), 400
    if k is None:
        return jsonify(error= "k is missing"), 400
    
    return jsonify( answer= caeser_mod(word,int(k)) ), 200

@sara.route("/uncaeser", methods= ["GET", "POST"])
def uncaeser_flask():
    if request.method== "GET":
        vals= request.args
    elif request.method=="POST":
        vals= request.json
    else:
        return jsonify(error="Invalid method!"), 405 
    
    word= vals.get("word")
    k= vals.get("k")
    
    if word is None:
        return jsonify(error= "word is missing"), 400
    if k is None:
        return jsonify(error= "k is missing"), 400
    
    return jsonify( answer= caeser_unmod(word,int(k)) ), 200




