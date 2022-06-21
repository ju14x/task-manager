# task-manager

Task management software w/ FastAPI
Done following [cassiobotaro](https://github.com/cassiobotaro/do_zero_a_implantacao/)'s tutorial, for learning purposes.

### how to run

-   clone this repo
-   create the virtual environment:

```sh
python -m venv .venv
```

-   activate it:

```sh
source .venv/bin/activate # linux

.venv/Scripts/activate # windows
```

-   install base requirements:

```sh
pip install -r requirements.txt
```

-   or, to install development requirements:

```sh
pip install -r dev-requirements.txt
```

-   run on localhost:8000:

```sh
uvicorn --reload task_manager.manager:app
```

- execute tests:

```sh
python -m pytest
```