# ClubZoneApp

ClubZoneApp is a student club management system built with Python's Tkinter for the GUI and SQLite for the database. It allows students to log in, select clubs, and view events, while coordinators can log in and manage club events. 

## Features

- **Student Login**: Students can log in and view upcoming events from various clubs.
- **Coordinator Login**: Coordinators can log in to create, manage, and view events for their clubs.
- **Event Management**: Coordinators can add events for specific clubs that are visible to students.

## Prerequisites

Ensure you have the following installed before running the application:

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Pillow (`pip install pillow`)
- SQLite3 (comes pre-installed with Python)

## Installation
Follow these steps to set up and run the application on your local machine.

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ClubZoneApp.git
   cd ClubZoneApp
   ```
2.Install the required Python packages:
   ```bash
  pip install -r requirements.txt
```
3.Set up the SQLite database:

-Make sure to create the necessary tables in your SQLite databases. Use the following schema:
For 'student_login.db':
```sql
CREATE TABLE student (
    Username TEXT PRIMARY KEY,
    Password TEXT NOT NULL
);
```
For 'coordinator_login.db':
```sql
CREATE TABLE coordinator (
    Username TEXT PRIMARY KEY,
    Password TEXT NOT NULL
);
```
For 'Events.db':
```sql
CREATE TABLE events (
    event_name TEXT NOT NULL,
    club_name TEXT NOT NULL,
    event_date TEXT NOT NULL
);
```
4.Add initial data to the databases using an SQLite browser or programmatically.
# Usage
- Run the application:
  ```bash
  python ClubZoneApp.py
  ```
- The login screen will appear, where you can either log in as a Student or Coordinator.

- Students can select a club and view upcoming events.

- Coordinators can add events by entering event details such as event name, club name, and event date.
```ardunio
ClubZoneApp/
│
├── assets/
│   ├── background.png
│   └── screenshots/
│       ├── login_screen.png
│       ├── student_view.png
│       └── coordinator_view.png
│
├── student_login.db
├── coordinator_login.db
├── Events.db
├── ClubZoneApp.py
└── README.md
```
# Requirements
List of required Python libraries:

- Tkinter
- Pillow
- SQLite3 (pre-installed with Python)
# Contributing
Feel free to submit a pull request if you would like to contribute to this project.
# Contact
For any questions, feel free to reach out at [mohisinashaik2005@gmail.com].
```csharp

This `README.md` assumes the project is structured with assets, databases, and the main application file (`ClubZoneApp.py`). You can customize it further based on your specific project details.

```

  

