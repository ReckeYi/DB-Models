from sqlalchemy.orm import relationship
from .base import DeclBase
import sqlalchemy as sa

from db.engine import engine


class Project(DeclBase):
    __tablename__ = 'projects'
    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    title = sa.Column(sa.String(150), nullable=False)
    description = sa.Column(sa.String(500))
    status = sa.Column(sa.String(150), nullable=False)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='projects')

    def __init__(self, title: str, description: str, status: str, user_id: int):
        self.title = title
        self.description = description
        self.status = status
        self.user_id = user_id

# DeclBase.metadata.create_all(engine)
