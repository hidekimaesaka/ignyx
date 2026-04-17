from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from app.schemas.message import Message
from app.schemas.user import UserDB, UserList, UserPublic, UserSchema

router = APIRouter(prefix='/users')

fake_db = []


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):

    user_with_id = UserDB(**user.model_dump(), id=len(fake_db) + 1)

    fake_db.append(user_with_id)

    return user_with_id


@router.get('/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': fake_db}


@router.put('/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):

    if user_id > len(fake_db) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found!'
        )

    updated_user = UserDB(**user.model_dump(), id=user_id)
    fake_db[user_id - 1] = updated_user

    return updated_user


@router.delete('/{user_id}', status_code=HTTPStatus.OK, response_model=Message)
def delete_user(user_id: int):
    if user_id > len(fake_db) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found!'
        )

    del fake_db[user_id - 1]

    return {'message': 'User deleted!'}
