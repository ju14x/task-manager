from fastapi.testclient import TestClient
from task_manager.manager import app
from fastapi import status


def test_status_200():
    cliente = TestClient(app)
    resp = cliente.get('/tarefas')
    assert resp.status_code == status.HTTP_200_OK
