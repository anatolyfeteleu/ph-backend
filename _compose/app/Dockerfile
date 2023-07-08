FROM python:3.11

# [set working directory]
WORKDIR /app/code

# [set environment variables]
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

ENV SCRIPTS_PATH=./_compose/scripts
ENV PROJECT_PATH=/app/code

# [updating packages]
RUN apt update -y

# [installing system packages]
RUN apt install -y graphviz graphviz-dev gettext binutils libproj-dev gdal-bin

# [copying scripts]
COPY $SCRIPTS_PATH/start-app \
     $SCRIPTS_PATH/start-celery-workers /
RUN chmod +x /start-app \
             /start-celery-workers

# [installing requirements]
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-input setuptools poetry

COPY pyproject.toml poetry.lock /

RUN poetry config virtualenvs.create false
RUN poetry install --without production

# [copying codebase]
ADD . $PROJECT_PATH