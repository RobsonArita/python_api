from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.get('/', response_model=str)
def default_get():
  return 'Teste'