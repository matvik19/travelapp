from fastapi import APIRouter
from users.schemas import CreateUser

from users import crud

router = APIRouter(prefix="/users", tags=["users"])

users = [
    {"id": 1, "name": "Матвей"},
    {"id": 2, "name": "Андрей"},
    {"id": 3, "name": "Денис"},
]


@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)


@router.get("/{user_id}/")
def get_users_by_id(user_id: int):
    return [user for user in users if user.get("id") == user_id]
