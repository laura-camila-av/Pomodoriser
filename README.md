# Pomodoriser
Extension of previous Pomodoriser to a cleaner and more interactive interface.
# 🍅 Pomodoriser

Pomodoriser is a simple web application that helps users turn a list of tasks into a structured Pomodoro-style schedule. Users input tasks with estimated durations, and the app generates a clear, time-based plan to guide focused work sessions. This project was built to combine productivity techniques (Pomodoro method) with practical software design and aims to save planning time and maximise working time! 

This project was originally built as a command-line tool and later refactored into a web application to improve usability and accessibility.

---

## Features

* Add tasks with flexible time units (Pomodoro sessions, hours, or minutes)
* Automatically converts tasks into Pomodoro blocks
* Generates a structured schedule based on available time
* Dynamic timetable that updates based on user-selected start time
* Clean, readable UI for planning work sessions
* Optional notes field for each task

---

## Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript
* **Data Handling:** JSON (via Fetch API)
* **State Management:** Browser localStorage (for plan + notes)

---

## How It Works

1. The user enters their available time.
2. Tasks are added with a duration and unit.
3. The backend:

   * Converts all durations into Pomodoro sessions
   * Ensures the total plan fits within the available time
   * Expands tasks into individual Pomodoro blocks
4. The frontend:

   * Renders the plan as a timetable
   * Dynamically calculates time slots based on a chosen start time

---

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pomodoriser.git
cd pomodoriser
```

### 2. Install dependencies

```bash
pip install flask
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in browser

Go to:

```
http://127.0.0.1:5000/
```

---

## Planned Improvements

This project is actively being developed. Planned features include:

### Task Priority & Colour Coding

* Assign priority levels to tasks
* Visually distinguish tasks using colour-coded blocks

### Built-in Pomodoro Timer

* Automatic timer for work sessions and breaks
* Sync with the generated schedule
* Visual indicators for current session

### Distraction Blocking (Future)

* Block access to distracting websites during work sessions
* Enforce focus periods aligned with the schedule

---

## Status

Current version: MVP
Core functionality is complete, with UI and feature enhancements in progress.

---

## Contributions

This is a personal project, but feedback and suggestions are welcome!

---

## License

This project is open-source and available under the MIT License.
