<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Campus Life Simulator</title>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <style>
        body {
            margin: 0;
            font-family: sans-serif;
            background: #f5f5dc;
        }
        #container {
            display: grid;
            grid-template-columns: 200px 1fr;
            height: 100vh;
        }
        #menu {
            background: #333;
            color: #fff;
            padding: 10px;
        }
        #menu button {
            display: block;
            width: 100%;
            margin: 5px 0;
            padding: 10px;
            background: #555;
            border: none;
            color: #fff;
            cursor: pointer;
            text-align: left;
        }
        #menu button:hover {
            background: #777;
        }
        #content {
            padding: 20px;
            overflow-y: auto;
        }
        .output {
            background: #fff8dc;
            padding: 15px;
            margin-top: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            white-space: pre-wrap;
            font-family: monospace;
        }
        .input-group {
            margin: 10px 0;
        }
        .input-group input, .input-group select {
            padding: 8px;
            margin: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .input-group button {
            padding: 8px 15px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .input-group button:hover {
            background: #45a049;
        }
        .section {
            margin-bottom: 20px;
            padding: 15px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>

<div id="container">
    <div id="menu">
        <h3>Campus Menu</h3>
        <button py-click="show_course()">Course Selection</button>
        <button py-click="show_library()">Library</button>
        <button py-click="show_club()">Club Selection</button>
        <button py-click="show_expense()">Expense Tracking</button>
        <button py-click="show_study()">Study Planner</button>
        <button py-click="show_credit()">Credit System</button>
        <button py-click="show_time()">Current Time</button>
    </div>
    <div id="content">
        <div id="main_output">Select an option from the menu to start your campus life simulation!</div>
    </div>
</div>

<py-config>
packages = []
[[fetch]]
from = "./"
files = ["campus_life.py"]
</py-config>

<py-script>
from campus_life import *
from js import document

content = document.getElementById("main_output")

def show_output(html_content):
    content.innerHTML = html_content

def show_time(*args):
    show_output(f'<div class="output">{game_time.display_current_time()}</div>')

# === Course Selection ===
def show_course(*args):
    html = '''
    <div class="section">
        <h3>🎓 Course Selection System</h3>
        <div class="input-group">
            <input type="text" id="course_add" placeholder="Course code (e.g., FOREST202)">
            <button py-click="add_course_web()">Add Course</button>
        </div>
        <div class="input-group">
            <input type="text" id="course_remove" placeholder="Course code to remove">
            <button py-click="remove_course_web()">Remove Course</button>
        </div>
        <button py-click="refresh_courses()">Refresh Timetable</button>
        <div id="course_output"></div>
    </div>
    '''
    show_output(html)
    refresh_courses()

def add_course_web(*args):
    course_input = document.getElementById("course_add")
    course_number = course_input.value.strip()
    if course_number:
        result = add_course(course_number)
        course_input.value = ""
        output_div = document.getElementById("course_output")
        output_div.innerHTML = f'<div class="output">{result}</div>'
        refresh_courses()

def remove_course_web(*args):
    course_input = document.getElementById("course_remove")
    course_number = course_input.value.strip()
    if course_number:
        result = remove_course(course_number)
        course_input.value = ""
        output_div = document.getElementById("course_output")
        output_div.innerHTML = f'<div class="output">{result}</div>'
        refresh_courses()

def refresh_courses(*args):
    result = get_timetable()
    output_div = document.getElementById("course_output")
    if output_div:
        output_div.innerHTML = f'<div class="output">{result}</div>'

# === Library System ===
def show_library(*args):
    html = '''
    <div class="section">
        <h3>📚 Library System</h3>
        <div class="input-group">
            <input type="text" id="book_borrow" placeholder="Book title to borrow">
            <button py-click="borrow_book_web()">Borrow Book</button>
        </div>
        <div class="input-group">
            <input type="text" id="book_return" placeholder="Book title to return">
            <button py-click="return_book_web()">Return Book</button>
        </div>
        <button py-click="refresh_library()">Refresh Inventory</button>
        <div id="library_output"></div>
    </div>
    '''
    show_output(html)
    refresh_library()

def borrow_book_web(*args):
    book_input = document.getElementById("book_borrow")
    title = book_input.value.strip()
    if title:
        result = borrow_book(title)
        book_input.value = ""
        output_div = document.getElementById("library_output")
        output_div.innerHTML = f'<div class="output">{result}</div>'
        refresh_library()

def return_book_web(*args):
    book_input = document.getElementById("book_return")
    title = book_input.value.strip()
    if title:
        result = return_book(title)
        book_input.value = ""
        output_div = document.getElementById("library_output")
        output_div.innerHTML = f'<div class="output">{result}</div>'
        refresh_library()

def refresh_library(*args):
    result = show_inventory()
    output_div = document.getElementById("library_output")
    if output_div:
        output_div.innerHTML = f'<div class="output">{result}</div>'

# === Club Selection ===
def show_club(*args):
    html = '''
    <div class="section">
        <h3>🎯 Club Selection</h3>
        <div class="input-group">
            <select id="club_select">
                <option value="guitar">🎸 Guitar Club</option>
                <option value="basketball">🏀 Basketball Club</option>
                <option value="anime">🎌 Anime Club</option>
            </select>
            <button py-click="join_club_web()">Join Club</button>
        </div>
        <div id="club_output"></div>
    </div>
    '''
    show_output(html)
    result = get_clubs()
    output_div = document.getElementById("club_output")
    output_div.innerHTML = f'<div class="output">{result}</div>'

def join_club_web(*args):
    club_select = document.getElementById("club_select")
    choice = club_select.value
    result = join_club(choice)
    output_div = document.getElementById("club_output")
    output_div.innerHTML = f'<div class="output">{result}</div>'

# === Expense Tracking ===
def show_expense(*args):
    html = '''
    <div class="section">
        <h3>💰 Expense Tracking</h3>
        <div class="input-group">
            <input type="text" id="expense_item" placeholder="Item name">
            <input type="text" id="expense_cost" placeholder="Cost">
            <button py-click="add_expense_web()">Add Expense</button>
        </div>
        <button py-click="show_expense_summary()">Show Summary</button>
        <div id="expense_output"></div>
    </div>
    '''
    show_output(html)

def add_expense_web(*args):
    item_input = document.getElementById("expense_item")
    cost_input = document.getElementById("expense_cost")
    item = item_input.value.strip()
    cost = cost_input.value.strip()
    if item and cost:
        result = add_expense(item, cost)
        item_input.value = ""
        cost_input.value = ""
        output_div = document.getElementById("expense_output")
        output_div.innerHTML = f'<div class="output">{result}</div>'

def show_expense_summary(*args):
    result = get_expense_summary()
    output_div = document.getElementById("expense_output")
    output_div.innerHTML = f'<div class="output">{result}</div>'

# === Study Planner ===
def show_study(*args):
    html = '''
    <div class="section">
        <h3>📚 Study Planner</h3>
        <div class="input-group">
            <input type="text" id="study_title" placeholder="Subject/title">
            <input type="number" id="study_pages" placeholder="Total pages">
            <input type="text" id="study_end_date" placeholder="End date (YYYY-MM-DD)">
            <button py-click="create_study_plan_web()">Create Plan</button>
        </div>
        <div id="study_output"></div>
    </div>
    '''
    show_output(html)

def create_study_plan_web(*args):
    title_input = document.getElementById("study_title")
    pages_input = document.getElementById("study_pages")
    date_input = document.getElementById("study_end_date")
    title = title_input.value.strip()
    pages = pages_input.value.strip()
    end_date = date_input.value.strip()
    if title and pages and end_date:
        result = create_study_plan(title, pages, end_date)
        output_div = document.getElementById("study_output")
        output_div.innerHTML = f'<div class="output">{result}</div>'

# === Credit System ===
def show_credit(*args):
    html = '''
    <div class="section">
        <h3>🎓 Credit System</h3>
        <div class="input-group">
            <input type="text" id="student_id" placeholder="Student ID">
            <input type="text" id="student_name" placeholder="Student Name">
            <button py-click="add_student_web()">Add Student</button>
        </div>
        <div class="input-group">
            <input type="text" id="enroll_id" placeholder="Student ID">
            <input type="text" id="enroll_course" placeholder="Course Code">
            <button py-click="enroll_student_web()">Enroll Course</button>
        </div>
        <div class="input-group">
            <input type="text" id="view_id" placeholder="Student ID to view">
            <button py-click="view_student_web()">View Student</button>
        </div>
        <div id="credit_output"></div>
    </div>
    '''
    show_output(html)

def add_student_web(*args):
    sid_input = document.getElementById("student_id")
    name_input = document.getElementById("student_name")
    sid = sid_input.value.strip()
    name = name_input.value.strip()
    if sid and name:
        result = add_student(sid, name)
        sid_input.value = ""
        name_input.value = ""
        output_div = document.getElementById("credit_output")
        output_div.innerHTML = f'<div class="output">{result}</div>'

def enroll_student_web(*args):
    enroll_id_input = document.getElementById("enroll_id")
    course_input = document.getElementById("enroll_course")
    sid = enroll_id_input.value.strip()
    course = course_input.value.strip()
    if sid and course:
        result = enroll_student(sid, course)
        course_input.value = ""
        output_div = document.getElementById("credit_output")
        output_div.innerHTML = f'<div class="output">{result}</div>'

def view_student_web(*args):
    view_id_input = document.getElementById("view_id")
    sid = view_id_input.value.strip()
    if sid:
        result = view_student(sid)
        output_div = document.getElementById("credit_output")
        output_div.innerHTML = f'<div class="output">{result}</div>'

# Initialize with current time
show_time()
</py-script>

</body>
</html>
