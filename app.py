from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Acheter du cake", "done": False},
    {"id": 2, "title": "Réviser Flask", "done": True},
]

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    if title:
        new_id = tasks[-1]["id"] + 1 if tasks else 1
        tasks.append({"id": new_id, "title": title, "done": False})
    return redirect(url_for("home"))

@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break
    return redirect(url_for("home"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
