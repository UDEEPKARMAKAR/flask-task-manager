# Task Manager - Flask Mini Project

A simple web application built with Python Flask that lets users add tasks
with a priority, mark them as completed, delete them, and filter the list.

*Built by:* Udeep Karmakar

## Features
- Add tasks using an HTML form (POST)
- View all tasks and filter by All / Pending / Completed (GET)
- Mark tasks as done or delete them
- Priority levels: Low, Medium, High
- Input validation with friendly error messages
- Custom 404 page
- Shared layout using Jinja2 template inheritance

## Technologies Used
- Python 3
- Flask
- HTML, CSS (Jinja2 templates)

## Project Structure
```
my_flask_project/
   screenshots/
   static/
      style.css
   templates/
      404.html
      about.html
      base.html
      index.html
      tasks.html
   app.py
   README.md
   requirements.txt

```

## Routes
| Route | Method | Purpose |
|---|---|---|
| `/` | GET | Homepage with add-task form |
| `/about` | GET | About page |
| `/tasks` | GET | List tasks (`?filter=all/pending/completed`) |
| `/add` | POST | Validate input and add a task |
| `/complete/<id>` | POST | Mark a task as completed |
| `/delete/<id>` | POST | Delete a task |

## Input Validation
- Task name cannot be empty or only spaces
- Task name must be 3 to 100 characters
- Priority must be Low, Medium or High
- Duplicate pending tasks are not allowed

## How to Run

1. Open a terminal in the project folder.
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the app:
   ```
   python app.py
   ```
6. Open http://127.0.0.1:5000 in your browser.

## Screenshots

### Homepage
![Home](screenshots/1_homepage.jpeg)

### Task added
![Task added](screenshots/2_task_added.jpeg)

### Empty input error
![Empty error](screenshots/3_empty_error.jpeg)

### Short input error
![Short error](screenshots/4_short_error.jpeg)

### Duplicate error
![Duplicate error](screenshots/5_duplicate_error.jpeg)

### Filters
![Filters](screenshots/6_filters.jpeg)

### About page
![About](screenshots/7_about.jpeg)

### 404 page
![404](screenshots/8_404.jpeg)

## Limitations
- Tasks are stored in memory, so they are lost when the server restarts.
- No database or login system (optional for this project).

## Future Improvements
- Store tasks in an SQLite database
- Edit existing tasks
- Add due dates