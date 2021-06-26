from starlette.testclient import TestClient
from .conftest import client  # noqa


def test_healthcheck(client):
    res = client.get("/healthcheck")
    assert res.status_code == 200
    assert res.json() == {"healthcheck": True}


