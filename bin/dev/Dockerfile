FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DOCKER_BUILDKIT=0
ENV COMPOSE_DOCKER_CLI_BUILD=0
WORKDIR /code

ADD requirements.txt /requirements.txt

RUN pip install virtualenvwrapper
RUN python3 -m venv /venv
RUN /venv/bin/pip install -U pip
RUN /venv/bin/pip install --no-cache-dir -r /requirements.txt