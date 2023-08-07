from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# ENGINE
engine = create_engine('postgresql://postgres:asdasdasd@localhost:5432/task_tracker')
Session = sessionmaker(bind=engine)
session = Session()
