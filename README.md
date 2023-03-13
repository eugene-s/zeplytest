# Zeply Test Task

## Development

### Requirements

- Docker
- direnv
- Python ~3.10
- Poetry ~1.4

### Run from Docker

```bash
docker compose build app  # build application
docker compose up migrate  # run migrations
docker compose up -d app  # run app
```

### Installation

- Be sure having Python 3.10 in your env:

```bash
python3.10
```

- Setup python environment:

```bash
poetry install
```

- Activate shell:

```bash
poetry shell
```

- Run migrations:

```bash
cd src
python manage.py migrate
```

- Run the database:

```bash
docker compose up -d postgres
```

- Run the project:

```bash
cd src
python manage.py runserver
```
