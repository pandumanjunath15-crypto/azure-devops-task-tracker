from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Explore Azure DevOps", "completed": False},
    {"id": 2, "title": "Run the CI pipeline", "completed": False},
]
next_id = 3


@app.get("/health")
def health():
    return jsonify(status="healthy")


@app.get("/api/tasks")
def list_tasks():
    return jsonify(tasks)


@app.post("/api/tasks")
def create_task():
    global next_id
    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()
    if not title:
        return jsonify(error="A non-empty title is required"), 400
    task = {"id": next_id, "title": title, "completed": False}
    next_id += 1
    tasks.append(task)
    return jsonify(task), 201


@app.patch("/api/tasks/<int:task_id>")
def update_task(task_id):
    data = request.get_json(silent=True) or {}
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task is None:
        return jsonify(error="Task not found"), 404
    if "title" in data:
        title = str(data["title"]).strip()
        if not title:
            return jsonify(error="Title cannot be empty"), 400
        task["title"] = title
    if "completed" in data:
        if not isinstance(data["completed"], bool):
            return jsonify(error="completed must be a boolean"), 400
        task["completed"] = data["completed"]
    return jsonify(task)


@app.delete("/api/tasks/<int:task_id>")
def delete_task(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task is None:
        return jsonify(error="Task not found"), 404
    tasks.remove(task)
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT", "5000")))
