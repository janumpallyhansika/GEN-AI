

import os
from pathlib import Path
from datetime import datetime, timezone

from dotenv import load_dotenv
from pymongo import MongoClient

# Load .env from the same folder as this Python file
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)


class UsageLogger:

    def __init__(self):
        mongo_uri = os.getenv("MONGODB_URI")

        if not mongo_uri:
            raise ValueError("MONGODB_URI not found in .env")

        self.client = MongoClient(
            mongo_uri,
            serverSelectionTimeoutMS=10000
        )

        # Test MongoDB connection
        self.client.admin.command("ping")

        # Select database and collection
        self.db = self.client["llm_monitoring"]
        self.collection = self.db["api_usage"]

        print("MongoDB connected successfully!")

    def log_call(self, data):
        try:
            log_data = data.copy()
            log_data["timestamp"] = datetime.now(timezone.utc)

            self.collection.insert_one(log_data)

            print("API usage logged successfully!")

        except Exception as e:
            print("Error logging API usage:", e)

    def close(self):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")
