from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-this-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL",
    "sqlite:///" + os.path.join(app.instance_path, "helpdesk.db")
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

os.makedirs(app.instance_path, exist_ok=True)
db = SQLAlchemy(app)


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requester_name = db.Column(db.String(100), nullable=False)
    requester_email = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    priority = db.Column(db.String(20), nullable=False, default="Medium")
    status = db.Column(db.String(30), nullable=False, default="Open")
    assigned_to = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey("ticket.id"), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


@app.route("/")
def dashboard():
    total = Ticket.query.count()
    open_count = Ticket.query.filter_by(status="Open").count()
    progress_count = Ticket.query.filter_by(status="In Progress").count()
    resolved_count = Ticket.query.filter_by(status="Resolved").count()
    critical_count = Ticket.query.filter_by(priority="Critical").count()
    recent_tickets = Ticket.query.order_by(Ticket.created_at.desc()).limit(8).all()
    return render_template(
        "dashboard.html",
        total=total,
        open_count=open_count,
        progress_count=progress_count,
        resolved_count=resolved_count,
        critical_count=critical_count,
        recent_tickets=recent_tickets,
    )


@app.route("/tickets")
def tickets():
    query = Ticket.query
    search = request.args.get("search", "").strip()
    status = request.args.get("status", "").strip()
    priority = request.args.get("priority", "").strip()
    category = request.args.get("category", "").strip()

    if search:
        pattern = f"%{search}%"
        query = query.filter(
            db.or_(
                Ticket.title.ilike(pattern),
                Ticket.requester_name.ilike(pattern),
                Ticket.requester_email.ilike(pattern),
                Ticket.description.ilike(pattern),
            )
        )
    if status:
        query = query.filter_by(status=status)
    if priority:
        query = query.filter_by(priority=priority)
    if category:
        query = query.filter_by(category=category)

    all_tickets = query.order_by(Ticket.created_at.desc()).all()
    return render_template(
        "tickets.html",
        tickets=all_tickets,
        search=search,
        selected_status=status,
        selected_priority=priority,
        selected_category=category,
    )


@app.route("/tickets/new", methods=["GET", "POST"])
def new_ticket():
    if request.method == "POST":
        required = ["title", "description", "requester_name", "requester_email", "category", "priority"]
        if any(not request.form.get(field, "").strip() for field in required):
            flash("Please complete all required fields.", "danger")
            return render_template("new_ticket.html")

        ticket = Ticket(
            title=request.form["title"].strip(),
            description=request.form["description"].strip(),
            requester_name=request.form["requester_name"].strip(),
            requester_email=request.form["requester_email"].strip(),
            category=request.form["category"],
            priority=request.form["priority"],
            status="Open",
            assigned_to=request.form.get("assigned_to", "").strip() or None,
        )
        db.session.add(ticket)
        db.session.commit()
        flash(f"Ticket #{ticket.id} created successfully.", "success")
        return redirect(url_for("ticket_detail", ticket_id=ticket.id))

    return render_template("new_ticket.html")


@app.route("/tickets/<int:ticket_id>", methods=["GET", "POST"])
def ticket_detail(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)

    if request.method == "POST":
        action = request.form.get("action")

        if action == "update":
            ticket.status = request.form["status"]
            ticket.priority = request.form["priority"]
            ticket.category = request.form["category"]
            ticket.assigned_to = request.form.get("assigned_to", "").strip() or None
            db.session.commit()
            flash("Ticket updated successfully.", "success")

        elif action == "comment":
            author = request.form.get("author", "").strip()
            message = request.form.get("message", "").strip()
            if author and message:
                db.session.add(Comment(ticket_id=ticket.id, author=author, message=message))
                db.session.commit()
                flash("Comment added.", "success")
            else:
                flash("Author and comment are required.", "danger")

        return redirect(url_for("ticket_detail", ticket_id=ticket.id))

    comments = Comment.query.filter_by(ticket_id=ticket.id).order_by(Comment.created_at.desc()).all()
    return render_template("ticket_detail.html", ticket=ticket, comments=comments)


@app.route("/tickets/<int:ticket_id>/delete", methods=["POST"])
def delete_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    Comment.query.filter_by(ticket_id=ticket.id).delete()
    db.session.delete(ticket)
    db.session.commit()
    flash(f"Ticket #{ticket.id} deleted.", "success")
    return redirect(url_for("tickets"))


@app.context_processor
def inject_now():
    return {"current_year": datetime.utcnow().year}


if __name__ == "__main__":
    app.run(debug=True)
