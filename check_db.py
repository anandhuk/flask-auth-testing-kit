
import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables from .env file
load_dotenv()

# Read the DATABASE_URL
DB_URL = os.getenv("DB_URL")

# Connect to PostgreSQL
conn = psycopg2.connect(DB_URL)
cursor = conn.cursor()
cursor.execute("SELECT version();")
print(cursor.fetchone())

cursor.close()
conn.close()