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


def test_update_user(client, user, token):

    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
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
        'id': user.id,
    }


def test_update_integrity_error(client, user, token):
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
        headers={'Authorization': f'Bearer {token}'},
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


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}


# TODO
# def test_email_not_in_jwt
# def test_email_sent_in_jwt_but_none_user_found
# def test_create_user_exist_email
# def test_create_user_exist_username
