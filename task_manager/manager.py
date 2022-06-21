from enum import Enum
from uuid import UUID, uuid4

from fastapi import FastAPI, status
from pydantic import BaseModel, constr

app = FastAPI()


class PossibleStates(str, Enum):
    done = "done"
    unfinished = "unfinished"


class EntryTask(BaseModel):
    title: constr(min_length=3, max_length=50)
    description: constr(max_length=140)
    state: PossibleStates = PossibleStates.unfinished


class Task(EntryTask):
    id: UUID


TASKS = []


@app.get("/tasks")
def list_tasks():
    return TASKS


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: EntryTask):
    new_task = task.dict()
    new_task.update({"id": uuid4()})
    return new_task
