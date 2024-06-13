from flask import Blueprint, jsonify
import requests

muayad2 = Blueprint("muayad2", __name__, url_prefix="/api/mw")

URL = "https://jsonplaceholder.typicode.com"

def fetch_todos():
    response = requests.get(URL + "/todos")
    if response.status_code // 100 != 2:
        print("Failed to fetch todos")
        response.raise_for_status()
    return response.json()

def fetch_posts():
    response = requests.get(URL + "/posts")
    if response.status_code // 100 != 2:
        print("Failed to fetch posts")
        response.raise_for_status()
    return response.json()

def fetch_post_comments(post_id):
    response = requests.get(f"{URL}/posts/{post_id}/comments")
    if response.status_code // 100 != 2:
        print(f"Failed to fetch comments for post {post_id}")
        response.raise_for_status()
    return response.json()

@muayad2.route("/todos", methods=["GET"])
def todos_route():
    todos_data = fetch_todos()
    return jsonify(todos_data)

@muayad2.route("/posts", methods=["GET"])
def posts_route():
    posts_data = fetch_posts()
    return jsonify(posts_data)

@muayad2.route("/posts/<int:post_id>/comments", methods=["GET"])
def post_comments_route(post_id):
    comments_data = fetch_post_comments(post_id)
    return jsonify(comments_data)




