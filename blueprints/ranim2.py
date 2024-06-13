from flask import Blueprint, jsonify,request
import requests

ranim2= Blueprint("ranim2", __name__, url_prefix="/api/ranim")

@ranim2.route("/user/<user_id>/todos", methods=["GET"])
def todos_flask(user_id):
    response= requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/todos")
    
    if request.method == "GET":
        values= request.args
    else:
        return jsonify(error="Invalid method!"), 405
    
    if user_id is None:
        return jsonify(error="Missing `user id`"), 400
    
    if int(response.status_code)//100 !=2:
         return jsonify(error="Invalid request!")
    
    return response.json()

@ranim2.route("/user/<user_id>/posts", methods=["GET"])
def posts_flask(user_id):
    response= requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/posts")
    
    if request.method == "GET":
        values= request.args
        
    else:
        return jsonify(error="Invalid method!"), 405
    

    if user_id is None:
        return jsonify(error="Missing `user id`"), 400
    
    if int(response.status_code)//100 !=2:
         return jsonify(error="Invalid request!")
    
    return response.json()

@ranim2.route("/user/<user_id>/posts/comments", methods=["GET"])
def comments_flask(user_id):
    response= requests.get(f"https://jsonplaceholder.typicode.com/posts/{user_id}/comments")
    
    if request.method == "GET":
        values= request.args
    else:
        return jsonify(error="Invalid method!"), 405
    
    if user_id is None:
        return jsonify(error="Missing `user id`"), 400
    
    if int(response.status_code)//100 !=2:
         return jsonify(error="Invalid request!")
    
    return response.json()


@ranim2.route("/users/todos", methods=["GET"])
def all_users_todos():
    response= requests.get(f"https://jsonplaceholder.typicode.com/todos")
    
    if request.method == "GET":
        values= request.args
    else:
        return jsonify(error="Invalid method!"), 405
    
    if int(response.status_code)//100 !=2:
         return jsonify(error="Invalid request!")
    
    return response.json()