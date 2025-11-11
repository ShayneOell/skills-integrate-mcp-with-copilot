import os
from pymongo import MongoClient
from typing import Iterator


MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:mongo@mongo:27017")
DB_NAME = os.getenv("MONGO_DB", "mergington")


def get_client() -> MongoClient:
	"""Return a MongoClient configured from environment variables."""
	return MongoClient(MONGO_URI)


def get_db() -> MongoClient:
	"""Return the database instance."""
	client = get_client()
	return client[DB_NAME]


def activities_collection():
	"""Convenience accessor for the activities collection."""
	return get_db()["activities"]


if __name__ == "__main__":
	print("This module provides helpers to access MongoDB. Import from code.")
