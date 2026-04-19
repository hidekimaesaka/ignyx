from http import HTTPStatus

from app.schemas.user import UserPublic


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@mail.com',
            'password': 'supersecret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@mail.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):

    response = client.put(
        '/users/1',
        json={
            'username': 'homensalame',
            'email': 'homensalame@example.com',
            'password': 'salame',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'homensalame',
        'email': 'homensalame@example.com',
        'id': 1,
    }


def test_update_integrity_error(client, user):
    client.post(
        '/users',
        json={
            'username': 'leclerc',
            'email': 'leclerc@example.com',
            'password': 'ferrari',
        },
    )

    response_update = client.put(
        f'/users/{user.id}',
        json={
            'username': 'leclerc',
            'email': 'leclerc@example.com',
            'password': 'salame',
        },
    )

    assert response_update.status_code == HTTPStatus.CONFLICT
    assert response_update.json() == {
        'detail': 'Username or Email already exists'
    }


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}


# TODO
# def test_update_not_existent_user
# def test_delete_not_existent_user
# def test_create_user_exist_email
# def test_create_user_exist_username
