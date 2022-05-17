from fastapi import FastAPI

app = FastAPI()
TASKS = [
    {
        "id": "1",
        "title": "shopping",
        "description": "buy milk and eggs",
        "state": "pending",
    },
    {
        "id": "2",
        "title": "study",
        "description": "TDD",
        "state": "ongoing",
    },
]


@app.get("/tasks")
def list_tasks():
    return TASKS
