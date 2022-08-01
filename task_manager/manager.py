from enum import Enum
from uuid import UUID, uuid4

from fastapi import FastAPI, status
from pydantic import BaseModel, constr

app = FastAPI()


class PossibleStates(str, Enum):
    done = 'done'
    unfinished = 'unfinished'


class EntryTask(BaseModel):
    title: constr(min_length=3, max_length=50)
    description: constr(max_length=140)
    state: PossibleStates = PossibleStates.unfinished


class Task(EntryTask):
    id: UUID


TASKS = []


@app.get('/tasks')
def list_tasks():
    return TASKS


@app.get(
    '/tasks/{task_id}',
    response_model=Task,
    status_code=status.HTTP_200_OK,
)
def get_task(task_id: UUID):
    for task in TASKS:
        if task['id'] == task_id:
            return task
    return status.HTTP_404_NOT_FOUND


@app.post('/tasks', response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: EntryTask):
    new_task = task.dict()
    new_task.update({'id': uuid4()})
    TASKS.append(new_task)
    return new_task


@app.delete('/tasks/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: UUID):
    for task in TASKS:
        if task['id'] == task_id:
            TASKS.remove(task)
    return status.HTTP_404_NOT_FOUND


@app.patch(
    '/tasks/{task_id}', response_model=Task, status_code=status.HTTP_200_OK
)
def complete_task(task_id: UUID):
    for task in TASKS:
        if task['id'] == task_id:
            task.update(state='done')
            return task
    return status.HTTP_422_UNPROCESSABLE_ENTITY
