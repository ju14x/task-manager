from fastapi.testclient import TestClient
from task_manager.manager import app, TASKS
from fastapi import status


def test_status_200():
    cliente = TestClient(app)
    resp = cliente.get('/tasks')
    assert resp.status_code == status.HTTP_200_OK


def test_return_json():
    cliente = TestClient(app)
    resp = cliente.get('/tasks')
    assert resp.headers['Content-Type'] == 'application/json'


def test_return_list():
    cliente = TestClient(app)
    resp = cliente.get('/tasks')
    assert isinstance(resp.json(), list)


def test_task_has_id():
    TASKS.append({'id': 1})
    cliente = TestClient(app)
    resp = cliente.get('/tasks')
    assert 'id' in resp.json().pop()
    TASKS.clear()


def test_task_has_title():
    TASKS.append({'title': 'title 1'})
    cliente = TestClient(app)
    resp = cliente.get('/tasks')
    assert 'title' in resp.json().pop()
    TASKS.clear()


def test_task_has_description():
    TASKS.append({'description': 'random description'})
    cliente = TestClient(app)
    resp = cliente.get('/tasks')
    assert 'description' in resp.json().pop()
    TASKS.clear()


def test_task_has_state():
    TASKS.append({'state': 'done'})
    cliente = TestClient(app)
    resp = cliente.get('/tasks')
    assert 'state' in resp.json().pop()
    TASKS.clear()
