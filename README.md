📚 Course Selection Tool

A Python Tkinter application that helps students (or users) select courses in a simple GUI.

✔ Load courses from a CSV file
✔ Filter by Year and Department
✔ Select up to 6 courses with automatic conflict detection
✔ Save selected courses into SavedCourses.csv

🚀 Features

🔎 Load & Filter Courses

Import a .csv file with course data

Filter by Year (1–5) and Department

📋 Interactive Course Lists

Available courses shown in one listbox

Double-click to add a course

Selected courses appear in a separate list

⚠ Smart Validation

Prevents duplicate course selections

Detects schedule conflicts (courses at the same time)

Maximum of 6 courses allowed

💾 Save Results

Selected courses can be saved as SavedCourses.csv

🛠 Requirements

Python 3.7+

Tkinter (comes with Python, no extra install needed)

📂 Project Structure
CourseTool/
│
├── main.py            # Main program (GUI)
├── README.md          # Documentation
└── SavedCourses.csv   # Created after saving (generated file)

▶ How to Run

Clone or download the repository.

Open a terminal in the project folder.

Run:

python main.py

📝 Usage Guide

Provide CSV Path → Enter the file path to your .csv course file.

Select Filters → Choose Year and type Department code (e.g., CS).

Click Display → Shows all matching courses.

Double-Click a Course → Adds it to your selection.

Review Selected Courses in the left listbox.

Save → Export selections to SavedCourses.csv.

📑 Example CSV Format

The .csv file should contain course details per row, like:

CS101 1, Introduction to Programming, Mon 10-12
MA202 2, Linear Algebra, Tue 14-16
PHY301 3, Physics III, Wed 09-11


First field: Course ID (Department + Number)

Second field: Year of study

Remaining fields: Course details (title, schedule, etc.)

📊 Example Workflow

Enter: C:/Users/John/Documents/courses.csv

Select Year = 2, Department = CS

Click Display → Courses for 2nd-year CS appear

Double-click CS202 → It appears in Selected Courses

Save → File SavedCourses.csv is created with your selection

📌 Notes

✅ Maximum 6 courses allowed

✅ Time conflicts between courses are automatically detected

⚠ Make sure your input .csv file is properly formatted

✨ With this tool, students can easily plan their schedules without worrying about overlaps or mistakes!
