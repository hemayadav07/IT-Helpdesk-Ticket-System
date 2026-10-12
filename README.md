# IT Help Desk Ticket Management System

A web-based IT Help Desk Ticket Management System built using Python and Flask to help IT support teams create, track, prioritize, and manage technical support requests efficiently.

## 🚀 Live Demo

**Live Application:** https://it-helpdesk-ticket-system-hema.onrender.com

## 📌 Project Overview

This project simulates a basic IT support ticketing workflow. Users can raise support tickets for technical issues, while support staff can manage ticket priorities, update statuses, assign tickets, and add troubleshooting notes.

## ✨ Features

* **Dashboard:** View total, open, in-progress, and resolved ticket statistics.
* **Ticket Creation:** Record issue details and requester information.
* **Ticket Management:** View, update, and delete support tickets.
* **Search & Filtering:** Find tickets by keyword, status, priority, and category.
* **Priority Management:** Categorize issues as Low, Medium, High, or Critical.
* **Status Tracking:** Manage tickets through Open, In Progress, Resolved, and Closed statuses.
* **Ticket Assignment:** Assign requests to an IT support team member.
* **Support Notes:** Add troubleshooting updates and resolution notes.
* **Database:** Store ticket records and comments using SQLite.

## 🛠️ Technologies Used

* **Backend:** Python, Flask
* **Database:** SQLite, Flask-SQLAlchemy
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Deployment:** Render, Gunicorn
* **Version Control:** Git, GitHub

## ⚙️ Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/hemayadav07/IT-Helpdesk-Ticket-System.git
   cd IT-Helpdesk-Ticket-System
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate it on Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python app.py
   ```

6. Open http://127.0.0.1:5000 in your browser.

## 🧪 Testing

Basic automated tests are included in the `tests/` directory. Run them with:

```bash
python -m unittest discover -s tests
```

## 🎯 Learning Outcomes

* Understanding IT support ticket workflows
* Building a web application with Python and Flask
* Working with relational data using SQLite and SQLAlchemy
* Implementing search, filtering, and ticket status management
* Using Git and GitHub for version control
* Deploying a Python web application on Render

## 👩‍💻 Author

**Hema Yadav**

GitHub: https://github.com/hemayadav07

---

*Created as a portfolio project for entry-level IT Support and Technical Support opportunities.*

