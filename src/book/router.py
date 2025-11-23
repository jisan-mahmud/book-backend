from fastapi import APIRouter, Request

router = APIRouter()

@router.get('/')
def books(request: Request):
    return {'success': True}