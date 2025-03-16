import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash

# Load environment variables
load_dotenv()
DB_URL = os.getenv("DB_URL")

# Create database engine
engine = create_engine(DB_URL)

# Define the base class for ORM models
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)

# Create the table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Test users data
test_users = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "user1", "password": "password1", "role": "user"},
    {"username": "user2", "password": "password2", "role": "user"},
    {"username": "user3", "password": "password3", "role": "user"},
    {"username": "user4", "password": "password4", "role": "user"},
]

# Insert users into the database
for user in test_users:
    hashed_password = generate_password_hash(user["password"])
    new_user = User(username=user["username"], password_hash=hashed_password, role=user["role"])
    session.add(new_user)

# Commit changes
session.commit()
print("Users added successfully!")

# Close the session
session.close()