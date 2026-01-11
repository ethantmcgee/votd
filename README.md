# Verse of the Day RSS Feed

A simple Flask application that fetches the Bible Gateway Verse of the Day and serves it as an RSS 2.0 feed.

## Docker Container

https://hub.docker.com/repository/docker/ethantmcgee/votd/

## Hosted Version

https://votd.ethantmcgee.com

## Features

- Fetches daily verse from Bible Gateway API
- Converts to standard RSS 2.0 format
- In-memory caching (1 hour TTL)
- Health check endpoint

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | RSS 2.0 feed |
| `/health` | Health check (returns "OK") |

## Running Locally

```bash
pip install -r requirements.txt
python app.py
```

The server starts on `http://localhost:8080`.

## Running with Docker

```bash
docker build -t votd .
docker run -p 8080:8080 votd
```

## Configuration

The application runs on port 8080 by default. In production, it uses Gunicorn as the WSGI server.
