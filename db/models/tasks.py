from sqlalchemy.orm import declarative_base, relationship
from .base import DeclBase
import sqlalchemy as sa
from db.engine import engine


class Task(DeclBase):
    __tablename__ = 'tasks'
    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    title = sa.Column(sa.String(150), nullable=False)
    description = sa.Column(sa.String(500))
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='tasks')
    deadline = sa.Column(sa.DateTime)
    status = sa.Column(sa.String(150), nullable=False)

    def __init__(self, title: str, description: str, user_id: int, deadline: sa.DateTime, status: str):
        self.title = title
        self.task_description = description
        self.user_id = user_id
        self.deadline = deadline
        self.status = status


# DeclBase.metadata.create_all(engine)
