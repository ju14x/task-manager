from fastapi import status
from fastapi.testclient import TestClient

from task_manager.manager import TASKS, app


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
    TASKS.append(
        {
            'id': 1,
            'title': 'title1',
            'description': 'description1',
            'state': 'done',
        }
    )
    cliente = TestClient(app)
    resp = cliente.get('/tasks')
    assert 'id' in resp.json().pop()
    TASKS.clear()


def test_task_has_title():
    TASKS.append(
        {
            'id': 1,
            'title': 'title1',
            'description': 'description1',
            'state': 'done',
        }
    )
    cliente = TestClient(app)
    resp = cliente.get('/tasks')
    assert 'title' in resp.json().pop()
    TASKS.clear()


def test_task_has_description():
    TASKS.append(
        {
            'id': 1,
            'title': 'title1',
            'description': 'description1',
            'state': 'done',
        }
    )
    cliente = TestClient(app)
    resp = cliente.get('/tasks')
    assert 'description' in resp.json().pop()
    TASKS.clear()


def test_task_has_state():
    TASKS.append(
        {
            'id': 1,
            'title': 'title1',
            'description': 'description1',
            'state': 'done',
        }
    )
    cliente = TestClient(app)
    resp = cliente.get('/tasks')
    assert 'state' in resp.json().pop()
    TASKS.clear()


def test_tasks_must_accept_post():
    cliente = TestClient(app)
    resp = cliente.post('/tasks')
    assert resp.status_code != status.HTTP_405_METHOD_NOT_ALLOWED


def test_submitted_task_must_have_title():
    cliente = TestClient(app)
    resp = cliente.post('/tasks', json={})
    assert resp.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_title_must_have_between_3_and_5_chars():
    cliente = TestClient(app)
    resp = cliente.post('/tasks', json={'title': 2 * '*'})
    assert resp.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    resp = cliente.post('/tasks', json={'title': 51 * '*'})
    assert resp.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_task_must_have_description():
    cliente = TestClient(app)
    resp = cliente.post(
        '/tasks', json={'title': 'title', 'description': '*' * 141}
    )
    assert resp.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_return_task_when_is_created():
    cliente = TestClient(app)
    expected_task = {'title': 'title', 'description': 'description'}
    resp = cliente.post('/tasks', json=expected_task)
    task_created = resp.json()
    assert task_created['title'] == expected_task['title']
    assert task_created['description'] == expected_task['description']
    TASKS.clear()


def test_created_task_id_must_be_unique():
    cliente = TestClient(app)
    task1 = {'title': 'title1', 'description': 'description1'}
    task2 = {'title': 'title2', 'description': 'description2'}
    resp1 = cliente.post('/tasks', json=task1)
    resp2 = cliente.post('/tasks', json=task2)
    assert resp1.json()['id'] != resp2.json()['id']
    TASKS.clear()


def test_created_task_default_state_is_unfinished():
    cliente = TestClient(app)
    task = {'title': 'title', 'description': 'description'}
    resp = cliente.post('/tasks', json=task)
    assert resp.json()['state'] == 'unfinished'
    TASKS.clear()


def test_created_task_status_code_must_be_201():
    cliente = TestClient(app)
    task = {'title': 'title', 'description': 'description'}
    resp = cliente.post('/tasks', json=task)
    assert resp.status_code == status.HTTP_201_CREATED
    TASKS.clear()


def test_created_task_must_be_persisted():
    cliente = TestClient(app)
    task = {'title': 'title', 'description': 'description'}
    cliente.post('/tasks', json=task)
    assert len(TASKS) == 1
    TASKS.clear()


def test_task_url_exists():
    cliente = TestClient(app)
    task = {'title': 'title', 'description': 'description'}
    resp = cliente.post('/tasks', json=task)
    task_created = resp.json()
    resp2 = cliente.get(f'/tasks/{task_created["id"]}')
    assert resp2.status_code == status.HTTP_200_OK
    TASKS.clear()


def test_delete_task():
    cliente = TestClient(app)
    task = {'title': 'title', 'description': 'description'}
    resp = cliente.post('/tasks', json=task)
    task_created = resp.json()
    resp2 = cliente.delete(f'/tasks/{task_created["id"]}')
    assert resp2.status_code == status.HTTP_204_NO_CONTENT
    TASKS.clear()


def test_mark_task_as_done():
    cliente = TestClient(app)
    task = {'title': 'title', 'description': 'description'}
    resp = cliente.post('/tasks', json=task)
    task_created = resp.json()
    resp2 = cliente.patch(
        f'/tasks/{task_created["id"]}', json={'state': 'done'}
    )
    assert resp2.status_code == status.HTTP_200_OK
    TASKS.clear()


def test_order_tasks_by_state():
    ...
