FROM python:3.9-slim-buster

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update -qq \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    apt-transport-https \
    apt-transport-https \
    build-essential \
    ca-certificates \
    curl \
    git \
    gnupg \
    jq \
    less \
    libpcre3 \
    libpcre3-dev \
    openssh-client \
    telnet \
    unzip \
    vim \
    wget \
    && apt-get clean \
    && rm -rf /var/cache/apt/archives/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && truncate -s 0 /var/log/*log

RUN pip install poetry

ENV PATH $PATH:/root/.poetry/bin

RUN pip install psycopg2-binary

RUN poetry config virtualenvs.create false
ENV PATH $PATH:/root/.poetry/bin

RUN mkdir -p /app
WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install  --no-interaction --no-ansi --with dev


ADD . /app
ENV DJANGO_SETTINGS_MODULE="task_manager.settings"

EXPOSE 8000

#RUN python manage.py makemigrations
#RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000
