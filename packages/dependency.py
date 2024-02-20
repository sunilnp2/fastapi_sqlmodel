from sqlmodel import Session
from packages.database import engine


def get_db():
    with Session(engine) as session:
        yield session
