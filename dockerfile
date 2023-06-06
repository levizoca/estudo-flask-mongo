FROM python:3.11-slim-buster

WORKDIR /python-docker

COPY pipfile* ./ /python-docker/

RUN pip install pipenv && pipenv install --system --deploy

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]