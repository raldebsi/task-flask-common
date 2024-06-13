from flask import Blueprint, jsonify, request
import requests

Tariq = Blueprint("Tariq", __name__, url_prefix="/api/Trq")

URL = "https://jsonplaceholder.typicode.com"


@Tariq.route("/todos", methods=["GET"])
def get_todos():
    response_todo = requests.get(URL + "/todos")
    if response_todo.status_code // 100 != 2:
        print("not ok")
        response_todo.raise_for_status()
    todo_data = response_todo.json()
    return jsonify(todo_data)


@Tariq.route("/posts", methods = ["GET"])
def get_posts():
    response_post = request.get(URL + "/post")
    if response_post.status_code // 100 != 2:
        print("not ok")
        response_post.raise_for_status()
    post_data = response_post.json()
    return jsonify(post_data)


@Tariq.route("/posts/<id>/comments", methods = ["GET"])
def get_posts_comment(id):
    response_post_id = request.get(URL +"/posts/{id}/comments")
    if response_post_id.status_code // 100 != 2:
        print("not ok")
        response_post_id.raise_for_status()
    post_id_data = response_post_id.json()
    return jsonify(post_id_data)