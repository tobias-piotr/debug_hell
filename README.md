# Debug Hell

Sample app for the VSCode debugging article

## Installation

Create a `.env` file. You can find an example in `/infra/example.env`.

Build Docker image

```shell
docker compose build
```

Start Docker containers

```shell
docker compose up
```

Both FastAPI app and Postgres database should be running.

To migrate the database tables, first exec into the FastAPI container

```shell
docker compose exec fastapi bash
```

And then, run the migration script

```shell
python debug_hell/database/migrate.py
```
