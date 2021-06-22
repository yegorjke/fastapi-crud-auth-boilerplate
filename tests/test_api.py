from api import __version__

from starlette.testclient import TestClient
from api.main import api

client = TestClient(api)

def test_version():
    assert __version__ == "0.1.0"

def test_index():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "hello world"}

def test_healthcheck():
    res = client.get("/healthcheck")
    assert res.status_code == 200
    assert res.json() == {"healthcheck": True}


