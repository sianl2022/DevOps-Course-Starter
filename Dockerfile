FROM python:3.8

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

COPY todo_app /app/todo_app 
WORKDIR /app
COPY pyproject.toml poetry.lock ./

ENTRYPOINT [ "/root/.local/bin/poetry", "run", "gunicorn", "--bind", "0.0.0.0", "'todo_app.app:create_app()'"]