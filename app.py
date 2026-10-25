from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (resets when the server restarts)
tasks = []
next_id = 1

PRIORITIES = ["Low", "Medium", "High"]

# Messages shown after an action (looked up by a short code in the URL)
MESSAGES = {
    "added": "Task added successfully!",
    "completed": "Task marked as completed.",
    "deleted": "Task deleted.",
    "notfound": "Sorry, that task was not found.",
}


def find_task(task_id):
    """Return the task with the given id, or None if it doesn't exist."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def get_stats():
    """Count total, completed and pending tasks."""
    done = len([t for t in tasks if t["done"]])
    return {"total": len(tasks), "done": done, "pending": len(tasks) - done}


@app.route("/")
def home():
    return render_template("index.html", priorities=PRIORITIES, stats=get_stats())


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/tasks")
def show_tasks():
    current_filter = request.args.get("filter", "all")

    if current_filter == "pending":
        shown = [t for t in tasks if not t["done"]]
    elif current_filter == "completed":
        shown = [t for t in tasks if t["done"]]
    else:
        current_filter = "all"
        shown = tasks

    message = MESSAGES.get(request.args.get("msg"))

    return render_template(
        "tasks.html",
        tasks=shown,
        stats=get_stats(),
        current_filter=current_filter,
        message=message,
    )


@app.route("/add", methods=["POST"])
def add_task():
    global next_id

    title = request.form.get("title", "").strip()
    priority = request.form.get("priority", "Medium")

    # ---- Validation ----
    error = None
    if not title:
        error = "Please enter a task name."
    elif len(title) < 3:
        error = "Task name must be at least 3 characters long."
    elif len(title) > 100:
        error = "Task name must be 100 characters or fewer."
    elif priority not in PRIORITIES:
        error = "Please choose a valid priority."
    elif any(t["title"].lower() == title.lower() and not t["done"] for t in tasks):
        error = "That task is already on your list."

    if error:
        # Show the form again with the error and keep what the user typed
        return render_template(
            "index.html",
            error=error,
            title=title,
            priority=priority,
            priorities=PRIORITIES,
            stats=get_stats(),
        )

    tasks.append({
        "id": next_id,
        "title": title,
        "priority": priority,
        "done": False,
        "created": datetime.now().strftime("%d %b %Y, %I:%M %p"),
    })
    next_id += 1

    # Redirect so refreshing the page doesn't submit the form twice
    return redirect(url_for("show_tasks", msg="added"))


@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    task = find_task(task_id)
    if task is None:
        return redirect(url_for("show_tasks", msg="notfound"))
    task["done"] = True
    return redirect(url_for("show_tasks", msg="completed"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    task = find_task(task_id)
    if task is None:
        return redirect(url_for("show_tasks", msg="notfound"))
    tasks.remove(task)
    return redirect(url_for("show_tasks", msg="deleted"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)