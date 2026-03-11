# Ping-Pong Service

A simple request counter service with PostgreSQL persistence, demonstrating StatefulSet usage in Kubernetes.

## Overview

This service increments and persists a counter each time it receives a request. The counter survives pod restarts by storing data in a PostgreSQL database.

## Features

- Request counting with database persistence
- RESTful API endpoints
- PostgreSQL StatefulSet for data storage
- Secrets management for database credentials

## Endpoints

### `GET /pingpong`
Increments counter and returns response

**Response:**
```
pong 1
```

### `GET /pings`
Returns current counter value (used by log-output service)

**Response:**
```json
{
  "pings": 5
}
```

## Tech Stack

- Python, Flask
- PostgreSQL (StatefulSet)
- Kubernetes (Secrets, StatefulSets, Services)

## Key Kubernetes Concepts

- StatefulSet for database deployment
- Secret management for credentials
- Persistent volumes for database storage
- Service exposure for inter-pod communication

## Deployment
```bash
# From repository root
kubectl apply -f manifests/
kubectl apply -f pingpong/manifests/
```

Access at: `http://localhost:8081/pingpong`

## Configuration

Requires a Secret with the following keys:
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`
- `POSTGRES_URL`

See `pingpong/manifests/secret.yaml` for template.

## Testing
```bash
# Make requests
curl http://localhost:8081/pingpong
# Returns: pong 1

curl http://localhost:8081/pingpong
# Returns: pong 2

# Verify persistence - delete pod and check counter continues
kubectl delete pod -n exercises <pingpong-pod>
curl http://localhost:8081/pingpong
# Counter should continue from where it left off
```