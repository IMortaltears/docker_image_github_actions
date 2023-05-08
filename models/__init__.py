from datetime import datetime
from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(120), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Entry {self.activity}>'
