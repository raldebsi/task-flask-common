from flask import Blueprint, request, jsonify
import requests

sara2= Blueprint("sara2", __name__, url_prefix="/api/sara")

@sara2.route('/user/<user_id>/todos', methods=["GET"])
def todos_user(user_id):
    response= requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/todos")

    if user_id is None:
        return jsonify(error= "user_id is None")
    
    if int(response.status_code)//100 != 2:
        return jsonify(error= "Invalid request")
    
    return response.json()

@sara2.route('/user/<user_id>/posts', methods=["GET"])
def posts_user(user_id):
    response= requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/posts")
    
    if user_id is None:
        return jsonify(error= "user_id is null")
    
    if int(response.status_code)//100 != 2:
        return jsonify(error= "Invalid request")
    
    return response.json()

@sara2.route('/user/<post_id>/comments', methods=["GET"])
def comments_user(post_id):
    response= requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
    
    if user_id is None:
        return jsonify(error= "user_id is None")
    
    if int(response.status_code)//100 != 2:
        return jsonify(error= "Invalid request")
    
    return response.json()

 
@sara2.route('/posts/todos', methods=["GET"])
def todos_all():
    response= requests.get(f"https://jsonplaceholder.typicode.com/todos")
    
    if int(response.status_code)//100 != 2:
        return jsonify(error= "Invalid request")
    
    return response.json()

@sara2.route('/posts', methods=["GET"])
def posts_all():
    response= requests.get(f"https://jsonplaceholder.typicode.com/posts")

    if int(response.status_code)//100 != 2:
        return jsonify(error= "Invalid request")
    
    return response.json()

@sara2.route('/comments', methods=["GET"])
def comments_all():
    response= requests.get(f"https://jsonplaceholder.typicode.com/comments")
    
    if int(response.status_code)//100 != 2:
        return jsonify(error= "Invalid request")
    
    return response.json()

    
    
    
    

   
    
    
    

