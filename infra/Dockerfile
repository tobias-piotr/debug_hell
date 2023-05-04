FROM python:3.11.3-slim-buster as base

# Expose port
EXPOSE 80

WORKDIR /code

# Set env variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="/code"

# Install necessary soft
RUN apt-get update \
    && apt-get install -y netcat curl git make gcc postgresql python3-dev libpq-dev \
    && apt-get clean

# Local development
FROM base as dev

ENV DEVELOPMENT=1

# Copy & install dependencies
COPY ./requirements ./requirements
RUN pip install -r ./requirements/dev.txt

COPY . .

CMD ["bash", "infra/run.sh"]

# Production environment
FROM base as prod

RUN useradd -mr debug_hell

USER debug_hell

ENV PATH=$PATH:/home/debug_hell/.local/bin

COPY --chown=debug_hell:debug_hell ./requirements ./requirements
RUN pip install -r ./requirements/prod.txt

COPY --chown=debug_hell:debug_hell . /code

CMD ["bash", "infra/run.sh"]
