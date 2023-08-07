from .users import User
from .tasks import Task
from .projects import Project
from .base import DeclBase
from sqlalchemy import MetaData

from db import engine


# DeclBase.metadata.create_all(engine)
# metadata = MetaData()

