import os
import tempfile
import unittest

from app import app, db, Ticket


class HelpdeskTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + self.db_path
        self.client = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_dashboard_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Support Dashboard", response.data)

    def test_create_ticket(self):
        response = self.client.post(
            "/tickets/new",
            data={
                "title": "Wi-Fi not working",
                "description": "Laptop cannot connect to office Wi-Fi.",
                "requester_name": "Demo User",
                "requester_email": "demo@example.com",
                "category": "Network",
                "priority": "High",
                "assigned_to": "IT Support",
            },
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        with app.app_context():
            self.assertEqual(Ticket.query.count(), 1)
            ticket = Ticket.query.first()
            self.assertEqual(ticket.status, "Open")


if __name__ == "__main__":
    unittest.main()
