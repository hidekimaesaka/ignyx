from dataclasses import asdict

from sqlalchemy import select

from app.models.user import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='George Russel',
            password='merc@',
            email='georgerussel59@mail.com',
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'George Russel'))
    assert asdict(user) == {
        'id': 1,
        'username': 'George Russel',
        'password': 'merc@',
        'email': 'georgerussel59@mail.com',
        'created_at': time,
    }
