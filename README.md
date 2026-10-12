# IT Help Desk Ticket Management System

A professional beginner-friendly IT support ticket management web application built with **Python, Flask, SQLite, SQLAlchemy, HTML, CSS and Bootstrap**.

## Features

- Dashboard with ticket KPIs
- Create support tickets
- Ticket search and filtering
- Priority management
- Status workflow: Open → In Progress → Resolved → Closed
- Ticket assignment
- Ticket detail page
- Internal support comments/notes
- Delete tickets
- SQLite database
- Responsive Bootstrap interface
- Production-ready Gunicorn configuration
- Render deployment configuration

## Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- Gunicorn
- Git/GitHub
- Render

## Run Locally

### 1. Create and activate virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use:

```powershell
.venv\Scripts\activate.bat
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Start the application

```powershell
python app.py
```

Open:

http://127.0.0.1:5000

The SQLite database is automatically created in the `instance` folder.

## Suggested Demo Workflow

1. Open Dashboard.
2. Create a ticket such as "Laptop cannot connect to Wi-Fi".
3. Select Hardware/Network category and High priority.
4. Assign it to "IT Support".
5. Open the ticket detail page.
6. Change status to "In Progress".
7. Add a support note.
8. Change status to "Resolved".
9. Return to Dashboard and verify the KPIs.

## GitHub

```powershell
git init
git add .
git commit -m "Initial IT help desk ticket management system"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Deployment on Render

1. Push this project to GitHub.
2. Create a Render account.
3. Create a new Web Service.
4. Connect the GitHub repository.
5. Use:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Deploy.
7. Open the generated `onrender.com` URL.

## Resume Project Description

**IT Help Desk Ticket Management System | Python, Flask, SQLite, SQLAlchemy, Bootstrap**
- Developed a full-stack IT support ticket management application for creating, tracking, filtering and resolving technical support requests.
- Implemented ticket lifecycle management with priority, category, assignment and status workflows.
- Built a dashboard with real-time ticket KPIs and a searchable/filterable ticket list.
- Added support comments and persistent relational data storage using SQLite and SQLAlchemy.
- Deployed the Flask application using Gunicorn and Render with Git/GitHub version control.
