from sqlmodel import create_engine
from packages.models import User, Blog
from sqlalchemy.orm import sessionmaker
# import sqlalchemy


DATABASE_URL = "postgresql://postgres:postgres@localhost/router"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create tables (automatically generated based on model definition)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

User.metadata.create_all(engine)
Blog.metadata.create_all(engine)
