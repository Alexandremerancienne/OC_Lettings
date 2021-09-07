FROM python:3.9

WORKDIR /oclettings

ENV PYTHONUNBUFFERED 1

ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]