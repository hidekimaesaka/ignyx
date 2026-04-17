from http import HTTPStatus


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
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@mail.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):

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


def test_not_update_not_found_when_invalid_id(client):
    response = client.put(
        '/users/4',
        json={
            'username': 'homensalame',
            'email': 'homensalame@example.com',
            'password': 'salame',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json().get('detail') == 'User not found!'


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}


def test_not_delete_not_found_when_invalid_id(client):
    response = client.delete('/users/4')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json().get('detail') == 'User not found!'
