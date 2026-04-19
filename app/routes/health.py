from http import HTTPStatus

from fastapi import APIRouter

from app.schemas.health_message import HealthMessage

router = APIRouter(tags=['health'])


@router.get('/', status_code=HTTPStatus.OK, response_model=HealthMessage)
def health_hello_message():
    return {'message': 'hello ignyx'}
