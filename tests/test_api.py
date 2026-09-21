from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["service"] == "CloudLatch"
    assert data["version"] == "1.0.0"
    assert data["environment"] == "development"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
    }


def test_readiness():
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ready",
        "service": "CloudLatch",
    }


def test_version():
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {
        "service": "CloudLatch",
        "version": "1.0.0",
    }