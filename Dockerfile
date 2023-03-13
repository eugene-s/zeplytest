FROM python:3.10-slim as python

WORKDIR /code

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=cache,target=/root/.cache/pypoetry/cache \
    --mount=type=cache,target=/root/.cache/pypoetry/artifacts \
    pip install poetry==1.4.0 && \
    poetry config virtualenvs.create false && \
    rm -rf /code/*

COPY poetry.lock pyproject.toml /code/

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=cache,target=/root/.cache/pypoetry/cache \
    --mount=type=cache,target=/root/.cache/pypoetry/artifacts \
    --mount=type=cache,target=/var/lib/apt/lists \
    apt-get update -qq && \
    apt-get install -q --yes --no-install-recommends \
    gcc \
    build-essential \
    && \
    poetry --no-root --no-interaction --no-ansi install \
    && \
    apt purge -q --yes gcc build-essential

FROM python as production

COPY src /code

ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0 --workers 3" \
    DJANGO_SETTINGS_MODULE=zeplytest.settings

CMD ["python", "-m", "gunicorn", "zeplytest.wsgi"]

FROM python as development

CMD ["sleep", "infinite"]
