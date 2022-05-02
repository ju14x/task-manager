from fastapi import FastAPI


app = FastAPI()


@app.get('/tarefas')
def list_tasks():
    return ''
