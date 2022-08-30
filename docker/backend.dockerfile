FROM python:3.9
WORKDIR /app

# 상대경로 절대경로 둘 다 가능
COPY ../app ./app

COPY ../Pipfile .
COPY ../Pipfile.lock .

RUN pip install pipenv

RUN pipenv install

CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000

