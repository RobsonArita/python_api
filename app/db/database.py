from pymongo import MongoClient
from ..core.config import settings

client = MongoClient(settings.mongodb_url)

database = client['RobsonDatabase']