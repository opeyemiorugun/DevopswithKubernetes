# Log Output Service

A multi-container Kubernetes application demonstrating shared volume communication between containers.

## Overview

This service consists of two containers running in a single pod:
- **Writer container**: Generates a random UUID on startup and writes timestamped logs to a shared file every 5 seconds
- **Reader container**: Serves an HTTP endpoint that reads the log file and displays its contents

## Features

- Multi-container pod with shared persistent volume
- ConfigMap integration for file content and environment variables
- HTTP endpoint displaying combined data from multiple sources
- Inter-service communication with ping-pong service

## Output Format

When accessing the service endpoint, you'll see:
```
file content: this text is from file
env variable: MESSAGE=hello world
2024-03-30T12:15:17.705Z: 8523ecb1-c716-4cb6-a044-b9e83bb98e43.
Ping / Pongs: 3
```

## Tech Stack

- Python, Flask
- Kubernetes (multi-container pods, persistent volumes, ConfigMaps)
- HTTP client for service communication

## Key Kubernetes Concepts

- Multi-container pods
- Shared volumes between containers
- ConfigMap mounting (file + env variable)
- Service-to-service communication via Kubernetes DNS

## Deployment
```bash
# From repository root
kubectl apply -f manifests/
kubectl apply -f log_output/manifests/
```

Access at: `http://localhost:8081/log`

## Configuration

The service reads configuration from:
- **ConfigMap**: `information.txt` file content and `MESSAGE` environment variable
- **Shared Volume**: Log file written by writer container
- **Service Discovery**: Ping-pong service at `http://pingpong-svc:2345/pings`