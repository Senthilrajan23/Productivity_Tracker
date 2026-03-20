# Productivity Tracker

A simple web-based productivity tracker built using Flask and SQLAlchemy to monitor time spent across different activities (AUX states).
 
---

## 🚀 Overview

This project helps track how time is spent throughout the day by allowing users to switch between different activity states such as:

- Learning
- Coding
- Break
- Available
- Entertainment
- Offline

Each activity is recorded with a start and end time, and the app calculates the total time spent in each category.

---

## 💡 Problem It Solves

We often assume we are productive, but we rarely measure where our time actually goes.

This app provides a simple way to:
- Track real-time activity
- Avoid duplicate tracking of the same activity
- Evaluate time distribution across tasks

---

## 🛠 Features

- Start and switch between AUX states
- Automatic time tracking using timestamps
- Prevent duplicate sessions for the same AUX
- Handle active sessions (no end time yet)
- Evaluate total time spent per AUX using aggregation queries
- Clean and simple UI

---

## 🧠 Key Learnings

While building this project, I learned:

- How Flask handles routes and user interactions
- Database design using SQLAlchemy ORM
- Writing aggregation queries (SUM, GROUP BY)
- Handling edge cases like active sessions
- Connecting backend logic with frontend UI
- Using Git for version control

---

## ⚙️ Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML (Jinja templates)

---

## 📂 Project Structure
Productivity_Tracker
│

├── templates/

│ └── base.html

│

├── main.py

├── requirements.txt

└── .gitignore


---

## ▶️ How to Run

1. Clone the repository:
git clone https://github.com/Senthilrajan23/Productivity_Tracker.git

2. Create a virtual environment (optional but recommended):
python -m venv .venv
.venv\Scripts\activate # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run the app:
python main.py

5. Open in browser:
http://127.0.0.1:5002/

---

## 📊 How It Works

- Each time an AUX is selected, a new session is created
- The previous active session is automatically closed
- Time is calculated using:
COALESCE(end_time, CURRENT_TIMESTAMP) - start_time
- Results are grouped by AUX and displayed to the user

---

## 📚 References

- Flask Documentation  
- SQLAlchemy Documentation  
- YouTube tutorials for backend basics  
- ChatGPT for debugging and understanding concepts

---

## 🚧 Future Improvements

- Add user authentication
- Detect inactivity
- Store data in PostgreSQL for production
- Add charts/graphs for visualization
- Export productivity reports
- Improve UI/UX

---

## 🙌 Acknowledgement

This project was built as part of my learning journey in backend development and web applications.
