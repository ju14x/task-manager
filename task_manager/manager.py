from fastapi import FastAPI

app = FastAPI()
TASKS = [
    {
        'id': '1',
        'title': 'shopping',
        'description': 'buy milk and eggs',
        'state': 'pending',
    },
]


@app.get('/tasks')
def list_tasks():
    return TASKS
