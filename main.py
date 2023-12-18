from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined To-Do items
todos = {
    1: {'id': 1, 'title': 'Buy groceries'},
    2: {'id': 2, 'title': 'Read a book'},
    3: {'id': 3, 'title': 'Exercise'}
}
current_id = 4  # Next ID to assign

# Create a new To-Do item
@app.route("/todos", methods=["POST"])
def create_todo():
    global current_id
    title = request.json.get('title')
    if not title:
        return jsonify({"error": "Title is required"}), 400

    todos[current_id] = {'id': current_id, 'title': title}
    current_id += 1
    return jsonify(todos[current_id - 1]), 201

# Get all To-Do items
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(list(todos.values()))

# Get a specific To-Do item
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = todos.get(todo_id)
    if not todo:
        return jsonify({"error": "To-Do not found"}), 404
    return jsonify(todo)

# Update a specific To-Do item
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = todos.get(todo_id)
    if not todo:
        return jsonify({"error": "To-Do not found"}), 404

    title = request.json.get('title')
    if not title:
        return jsonify({"error": "Title is required"}), 400

    todo['title'] = title
    return jsonify(todo)

# Delete a specific To-Do item
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    if todo_id not in todos:
        return jsonify({"error": "To-Do not found"}), 404

    del todos[todo_id]
    return jsonify({"message": "To-Do deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
