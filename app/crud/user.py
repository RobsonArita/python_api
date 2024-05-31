from pymongo.collection import Collection
from app.db.database import database
from app.schemas.user import UserCreate, User, UserUpdate
from bson import ObjectId
from typing import Optional
from datetime import datetime

users_collection: Collection = database.get_collection('users')

def create_user(user: UserCreate) -> User:
    now = datetime.now()
    user_data = user.model_dump()
    user_data["_id"] = str(ObjectId())
    user_data["createdAt"] = now
    user_data["updatedAt"] = now
    users_collection.insert_one(user_data)
    return User(id=user_data["_id"], email=user_data["email"], createdAt=user_data["createdAt"], updatedAt=user_data["updatedAt"])

def get_user_by_email(email: str) -> Optional[User]:
    user_data = users_collection.find_one({"email": email})
    if user_data:
        return User(id=user_data["_id"], email=user_data["email"], createdAt=user_data["createdAt"], updatedAt=user_data["updatedAt"])
    return None

def get_user(user_id: str) -> Optional[User]:
    user_data = users_collection.find_one({"_id": user_id})
    if user_data:
        return User(id=user_data["_id"], email=user_data["email"], createdAt=user_data["createdAt"], updatedAt=user_data["updatedAt"])
    return None

def delete_user(user_id: str) -> bool:
    result = users_collection.delete_one({"_id": user_id})
    return result.deleted_count == 1

def update_user(user_id: str, user: UserUpdate) -> Optional[UserUpdate]:
    user_data = user.model_dump()
    user_data["updatedAt"] = datetime.now()
    result = users_collection.update_one(
        {"_id": user_id},
        {"$set": user_data}
    )
    if result.modified_count == 1:
        return user
    return None