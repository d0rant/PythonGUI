Course Tool

This project is a Course Selection Tool built with Python Tkinter.
It allows students (or users) to:

Load available courses from a CSV file.

Filter courses by Year and Department.

Select up to 6 courses while preventing time conflicts.

Save selected courses into a new CSV file.

The tool provides a simple graphical user interface (GUI) for better usability.

Features

Load courses from CSV
Enter the path of a .csv file containing course data.

Filter by Year and Department

Choose study year (1–5).

Enter department code (e.g., "CS").

Course Display
Filtered courses are displayed in a listbox.

Double-click a course to select it.

The tool prevents duplicate selections.

A warning is shown if two courses overlap in time.

You may select up to six courses only.

Buttons

Display → Loads and filters courses.

Clear → Clears all selected courses.

Save → Saves selected courses into SavedCourses.csv.

Selected Courses View

Shows all courses chosen by the user.

Requirements

Python 3.x

Tkinter (comes pre-installed with Python)

No external libraries are needed.

File Structure
CourseTool/
│
├── main.py           # Main program
├── SavedCourses.csv  # Created after saving selections
└── README.md         # Documentation

How to Run

Clone or download the repository.

Make sure your system has Python 3.x installed.

Open a terminal in the project folder.

Run the program:

python main.py

Usage

Enter the file path of your course CSV file in the entry box.
Example:

C:/Users/Name/Documents/courses.csv


Select the Year from the dropdown.

Enter the Department code (e.g., CS).

Click Display to load matching courses.

Double-click a course in the list to select it.

Review your chosen courses in the Selected Courses list.

Save selections by clicking Save.

Example CSV File Format

The CSV should contain course details in rows.
A sample line might look like:

CS101 1, Introduction to Programming, Mon 10-12
MA202 2, Linear Algebra, Tue 14-16


First field: Department + Course ID (e.g., CS101).

Second field: Year (e.g., 1, 2, 3).

Remaining fields: Course details (name, schedule, etc.).

Output

Selected courses are saved to SavedCourses.csv.

Each course is written as a row.

Notes

You can only select up to six courses.

If two courses have overlapping schedules, the tool will warn you.

Make sure your CSV file is well-formatted before using.
