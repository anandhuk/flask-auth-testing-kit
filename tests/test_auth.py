import pytest
from app import app, db
from app.models.user import User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            user = User(username="test-user", role="user")
            user.set_password("test-password")
            db.session.add(user)
            db.session.commit()
        yield client

def test_login(client):
    response = client.post("/auth/token", json={
        "client_id": "test-client",
        "code_verifier": "test-verifier"
    })
    assert response.status_code == 200
    assert "access_token" in response.json