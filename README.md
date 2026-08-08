# k8s

FastAPI book management service built with `uv` and `SQLModel`.

## Quick Start (Docker)

```bash
# Build
docker build -t k8s-app .

# Run
docker run -p 8000:8000 -e DATABASE_URL="sqlite:///./db/app.db" k8s-app
```

## Local Development

```bash
uv sync
DATABASE_URL="sqlite:///./db/app.db" uv run uvicorn main:app --reload
```

## API Endpoints

- `POST /api/v1/book/create`
- `GET /api/v1/book/books`
- `GET /api/v1/book/books/{book_id}`
