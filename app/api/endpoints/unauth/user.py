from fastapi import APIRouter, Depends, HTTPException
from app.crud.user import create_user, get_user_by_email, get_user, delete_user, update_user
from app.schemas.user import UserCreate, User, UserUpdate, UserDelete

router = APIRouter()

@router.get('/', response_model=str)
def default_get():
  return 'Teste'


@router.post("/", response_model=User)
def create_user_api(user: UserCreate):
    db_user = get_user_by_email(user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(user)

@router.get("/{user_id}", response_model=User)
def read_user(user_id: str):
    db_user = get_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=UserUpdate)
def update_user_api(user_id: str, user: UserUpdate):
    db_user = update_user(user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=UserDelete)
def delete_user_api(user_id: str):
    success = delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return UserDelete(success=success)