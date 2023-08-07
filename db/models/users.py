from sqlalchemy.orm import declarative_base
from .base import DeclBase
import sqlalchemy as sa
from db.engine import engine


class User(DeclBase):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    username = sa.Column(sa.String(50), unique=True, nullable=False)
    email = sa.Column(sa.String(50), unique=True, nullable=False)
    role = sa.Column(sa.String(15), nullable=False)

    def __init__(self, username: str, email: str, role: str):
        self.username = username
        self.email = email
        self.role = role


# DeclBase.metadata.create_all(engine)
