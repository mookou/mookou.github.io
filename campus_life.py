# campus_life.py
import time
from datetime import datetime, timedelta
import math

# =========================
# Game Time System
# =========================
class GameTime:
    def __init__(self):
        self.start_time = datetime.now()
        self.game_time = self.start_time
        self.time_multiplier = 10  # 遊戲時間流逝速度 (現實1秒 = 遊戲10秒)
        
    def update_time(self, action_duration_minutes=0):
        """更新遊戲時間，並顯示當前時間"""
        # 計算現實時間流逝
        real_time_passed = datetime.now() - self.start_time
        # 轉換為遊戲時間流逝
        game_seconds_passed = real_time_passed.total_seconds() * self.time_multiplier
        self.game_time = self.start_time + timedelta(seconds=game_seconds_passed)
        
        # 如果指定了行為耗時，則增加遊戲時間
        if action_duration_minutes > 0:
            self.game_time += timedelta(minutes=action_duration_minutes)
            
        return self.game_time
    
    def display_current_time(self):
        """顯示當前遊戲時間"""
        current_time = self.update_time()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"🕐 當前遊戲時間: {formatted_time}"
    
    def perform_action(self, action_name, duration_minutes):
        """執行一個消耗時間的行為"""
        result = []
        result.append(f"⏳ 正在執行: {action_name}...")
        result.append(f"⏰ 預計耗時: {duration_minutes} 分鐘")
        
        # 顯示行動前的時間
        result.append(self.display_current_time())
        
        # 更新時間（消耗時間）
        new_time = self.update_time(duration_minutes)
        formatted_time = new_time.strftime("%Y-%m-%d %H:%M:%S")
        
        result.append(f"✅ {action_name} 完成!")
        result.append(f"🕐 現在時間: {formatted_time}")
        
        return "\n".join(result)

# 創建全局遊戲時間實例
game_time = GameTime()

# =========================
# Course Selection System
# =========================
course_catalogue = {
    "FOREST202": "Exploring Taiwan: Natural Environment and Resources",
    "PH150": "Aerospace Fundamentals",
    "EN300": "Shakespeare Literature"
}

timetable = {
    "PP210": "Python Programming Foundation",
    "QF101": "Principles of Quantitative Finance"
}

def add_course(course_number):
    result = []
    if course_number in course_catalogue:
        timetable[course_number] = course_catalogue[course_number]
        result.append(f"Course {course_number} - {course_catalogue[course_number]} was added to your timetable.")
        # 選課消耗時間
        result.append(game_time.perform_action(f"選修課程 {course_number}", 30))
    else:
        result.append(f"Course {course_number} not found in the catalogue.")
    return "\n".join(result)

def remove_course(course_number):
    result = []
    if course_number in timetable:
        removed_course = timetable[course_number]
        del timetable[course_number]
        result.append(f"Course {course_number} - {removed_course} was removed from your timetable.")
        # 退課消耗時間
        result.append(game_time.perform_action(f"退選課程 {course_number}", 15))
    else:
        result.append(f"Course {course_number} not found in your timetable.")
    return "\n".join(result)

def get_timetable():
    result = []
    result.append(game_time.display_current_time())
    result.append("Current timetable:")
    for course, name in timetable.items():
        result.append(f"  - {course}: {name}")
    result.append("\nAvailable catalogue:")
    for course, name in course_catalogue.items():
        result.append(f"  - {course}: {name}")
    return "\n".join(result)

# =========================
# Library System
# =========================
inventory = {
    "1984": 2,
    "Dune": 1,
    "Germany: The Long Road West": 3,
    "The Pragmatic Programmer": 2
}

borrowed_by_user = {title: 0 for title in inventory}

def show_inventory():
    result = []
    result.append(game_time.display_current_time())
    result.append("Current library inventory (available / you have):")
    for title in inventory:
        result.append(f"  - {title}: {inventory[title]} available | you have {borrowed_by_user[title]}")
    return "\n".join(result)

def borrow_book(title: str):
    result = []
    if title not in inventory:
        result.append("This title does not exist in the library.")
        return "\n".join(result)
    if inventory[title] <= 0:
        result.append("No copies available at the moment.")
        return "\n".join(result)
    inventory[title] -= 1
    borrowed_by_user[title] += 1
    result.append(f"You borrowed '{title}'. Enjoy reading!")
    # 借書消耗時間
    result.append(game_time.perform_action(f"借閱書籍 '{title}'", 20))
    return "\n".join(result)

def return_book(title: str):
    result = []
    if title not in inventory:
        result.append("This title does not belong to this library.")
        return "\n".join(result)
    if borrowed_by_user[title] <= 0:
        result.append("You don't have this book to return.")
        return "\n".join(result)
    borrowed_by_user[title] -= 1
    inventory[title] += 1
    result.append(f"Thank you for returning '{title}'.")
    # 還書消耗時間
    result.append(game_time.perform_action(f"歸還書籍 '{title}'", 15))
    return "\n".join(result)

# =========================
# Club Selection
# =========================
def join_club(choice):
    result = []
    result.append(game_time.display_current_time())
    if choice == "guitar":
        result.append("Great choice! The Guitar Club meets every Wednesday evening.")
        result.append(game_time.perform_action("參加吉他社", 120))
    elif choice == "basketball":
        result.append("Awesome! The Basketball Club practices on Tuesdays and Fridays.")
        result.append(game_time.perform_action("參加籃球社", 120))
    elif choice == "anime":
        result.append("Nice! The Anime Club screens shows every Saturday afternoon.")
        result.append(game_time.perform_action("參加動漫社", 120))
    else:
        result.append("Sorry, that club is not available. Try 'guitar', 'basketball', or 'anime'.")
    return "\n".join(result)

def get_clubs():
    result = []
    result.append("Available clubs:")
    result.append("🎸 Guitar Club - Music and performance")
    result.append("🏀 Basketball Club - Sports and teamwork")  
    result.append("🎌 Anime Club - Japanese animation and culture")
    return "\n".join(result)

# =========================
# Expense Tracking
# =========================
expenses = []

def add_expense(item, cost):
    result = []
    try:
        cost_float = float(cost)
        expenses.append({"item": item, "cost": cost_float})
        result.append(f"Added: {item} - ${cost_float:.2f}")
        result.append(game_time.perform_action("記帳", 5))
    except ValueError:
        result.append("Invalid cost. Please enter a number.")
    return "\n".join(result)

def get_expense_summary():
    result = []
    result.append(game_time.display_current_time())
    if not expenses:
        result.append("No expenses recorded yet.")
        return "\n".join(result)
    
    total = sum(expense["cost"] for expense in expenses)
    count = len(expenses)
    avg = total / count
    
    result.append("Expense Summary:")
    result.append(f"Number of entries: {count}")
    result.append(f"Total spent: ${total:.2f}")
    result.append(f"Average per entry: ${avg:.2f}")
    result.append("\nBreakdown:")
    for expense in expenses:
        result.append(f" - {expense['item']}: ${expense['cost']:.2f}")
    return "\n".join(result)

# =========================
# Study Planner
# =========================
def create_study_plan(title, total_pages, end_date_str):
    result = []
    result.append(game_time.display_current_time())
    
    try:
        total_pages_int = int(total_pages)
        if total_pages_int <= 0:
            raise ValueError
    except ValueError:
        result.append("Total pages must be a positive integer.")
        return "\n".join(result)

    try:
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    except ValueError:
        result.append("End date format must be YYYY-MM-DD.")
        return "\n".join(result)

    today = datetime.now().date()
    days = (end_date - today).days + 1
    if days <= 0:
        result.append("End date must be today or a future date.")
        return "\n".join(result)

    pages_per_day = math.ceil(total_pages_int / days)

    result.append(f"Study Plan for '{title}'")
    result.append(f"From {today} to {end_date} ({days} days)")
    result.append(f"Target pages per day: {pages_per_day} (≈ {total_pages_int} pages total)")

    remaining = total_pages_int
    current = today
    day_idx = 1
    while remaining > 0 and current <= end_date:
        to_read = min(pages_per_day, remaining)
        result.append(f" Day {day_idx} ({current}): Read {to_read} pages")
        remaining -= to_read
        current += timedelta(days=1)
        day_idx += 1

    if remaining > 0:
        result.append(f" Extra: Read remaining {remaining} pages as needed.")
    
    result.append(game_time.perform_action("制定學習計劃", 45))
    return "\n".join(result)

# =========================
# Credit System
# =========================
class Student:
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.courses = set()
        self.credits = 0

    def enroll(self, course_number: str, course_name: str, credit_value: int):
        if course_number in self.courses:
            return f"[Duplicate prevented] {self.name} is already enrolled in {course_number}."
        self.courses.add(course_number)
        self.credits += credit_value
        return f"{self.name} enrolled in {course_number} - {course_name} (+{credit_value} credits)."

    def __repr__(self):
        return f"<Student {self.student_id} {self.name} | credits={self.credits} courses={sorted(self.courses)}>"

course_credits = {
    "FOREST202": 3,
    "PH150": 3,
    "EN300": 3,
    "PP210": 3,
    "QF101": 3,
}

students = {}

def add_student(student_id, name):
    result = []
    if not student_id or not name:
        return "ID and name are required."
    if student_id in students:
        return "Student ID already exists."
    students[student_id] = Student(student_id, name)
    result.append(f"Added: {students[student_id]}")
    result.append(game_time.perform_action("添加學生資料", 10))
    return "\n".join(result)

def enroll_student(student_id, course_no):
    result = []
    if student_id not in students:
        return "Unknown student. Add the student first."
    course_no = course_no.upper()
    if course_no not in course_catalogue:
        return "Course not found in the catalogue."
    credit_value = course_credits.get(course_no, 3)
    enrollment_result = students[student_id].enroll(course_no, course_catalogue[course_no], credit_value)
    result.append(enrollment_result)
    if "enrolled" in enrollment_result:
        result.append(game_time.perform_action(f"為學生 {student_id} 選課 {course_no}", 25))
    return "\n".join(result)

def view_student(student_id):
    result = []
    result.append(game_time.display_current_time())
    if student_id not in students:
        return "Unknown student."
    s = students[student_id]
    result.append(f"Student: {s.name} ({s.student_id})")
    result.append(f"Total credits: {s.credits}")
    if not s.courses:
        result.append("Enrolled courses: none")
    else:
        result.append("Enrolled courses:")
        for c in sorted(s.courses):
            cname = course_catalogue.get(c, "Unknown")
            result.append(f" - {c}: {cname} ({course_credits.get(c, 3)} credits)")
    result.append(game_time.perform_action("查看學生資料", 5))
    return "\n".join(result)
