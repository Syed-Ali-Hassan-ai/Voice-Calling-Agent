import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()  # Loads variables from .env file

MONGODB_URI = os.getenv("MONGODB_URI")
print(f"Connecting to MongoDB at: {MONGODB_URI}")  # Check if the URI is printed correctly

client = MongoClient(MONGODB_URI)
db = client.get_database()
