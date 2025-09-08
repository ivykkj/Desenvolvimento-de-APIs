from models import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Task(db.Model):

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Pendente")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="tasks")
    
    def __repr__(self):
        return f"<Task {self.title} - {self.status}>"
