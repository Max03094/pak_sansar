# tests/test_alerts.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..main import app, Base, engine as prod_engine
from ..dependencies import get_db_session

# Test DB
test_engine = create_engine("postgresql://user:pass@localhost/sansar_test_db")
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

Base.metadata.create_all(bind=test_engine)

async def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db_session] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_db():
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)

def test_create_alert(setup_db):
    response = client.post("/alerts/", json={"priority": 3, "type": "test", "description": "test desc", "military_office_id": 1})
    assert response.status_code == 200
    assert response.json()["type"] == "test"

# Similar tests for other endpoints