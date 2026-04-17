from http import HTTPStatus


def test_root_deve_retornar_ok_e_hello_ignify(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'hello ignyx'}  # Assert
