from flask import Flask, jsonify, request
app = Flask(__name__)


todos = [
    {"id": 1, "label": "Tarea num 1", "done": False},
    {"id": 2, "label": "Tarea num 2", "done": True}
]



@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

#GET por id
@app.route('/todos/<int:id>', methods=['GET'])
def get_todo_id(id):
    int_id = list(filter(lambda todo: todo['id'] == id, todos))
    print(int_id)
    return int_id

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    del todos[id]
    print("This is the id to delete:", id)
    return jsonify(todos)

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo_id(id):
    todo = next((todo for todo in todos if todo["id"] == id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    request_body = request.get_json()
    if "label" in request_body:
        todo["label"] = request_body["label"]
    if "done" in request_body:
        todo["done"] = request_body["done"]
    return jsonify(todo)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)