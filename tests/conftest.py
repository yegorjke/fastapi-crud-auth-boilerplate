import pytest
from starlette.testclient import TestClient

from app.main import app

@pytest.fixture(scope="module")
def client():
    client = TestClient(app)
    yield client
