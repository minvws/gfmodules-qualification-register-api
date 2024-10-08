# syntax=docker/dockerfile:1
# syntax directive is used to enable Docker BuildKit

ARG PYTHON_VERSION=3.11

FROM python:${PYTHON_VERSION}-slim AS base

ARG PROJECT_DIR="/src"
ARG APP_USER="app"
ARG APP_GROUP="app"
ARG NEW_UID
ARG NEW_GID

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  POETRY_CACHE_DIR=/tmp/poetry-cache \
  POETRY_VIRTUALENVS_CREATE=false

# Create a non-privileged user that the app will run under.
RUN groupadd --system ${APP_GROUP} --gid=${NEW_GID} && \
  adduser \
  --disabled-password \
  --gecos "" \
  --uid ${NEW_UID} \
  --gid ${NEW_GID} \
  ${APP_USER}

RUN apt update && \
  apt install -y \
  curl \
  iputils-ping \
  git \
  gnupg2 \
  make \
  postgresql-client-15 \
  postgresql-client-common \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN pip3 install --upgrade pip && \
  pip3 install poetry==1.8 --no-cache-dir

WORKDIR ${PROJECT_DIR}

FROM base AS builder

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry config repositories.git-minvws-gfmodules-python-shared-private https://github.com/minvws/gfmodules-python-shared-private.git
RUN --mount=type=secret,id=auth_toml,target=/root/.config/pypoetry/auth.toml \
  poetry lock --no-update
RUN --mount=type=cache,target=${POETRY_CACHE_DIR} \
  --mount=type=secret,id=auth_toml,target=/root/.config/pypoetry/auth.toml \
  poetry install --no-root --no-interaction

FROM base AS final

COPY --chown=${APP_USER}:${APP_GROUP} --from=builder /usr/local /usr/local

USER ${APP_USER}
WORKDIR ${PROJECT_DIR}

RUN poetry config repositories.git-minvws-gfmodules-python-shared https://github.com/minvws/gfmodules-python-shared.git

EXPOSE 8507:8507

ENV PYTHONPATH=${PROJECT_DIR}

CMD python -m app.main
