# Cloud-Native Todo Application with Automated Content Generation

A Kubernetes-native todo application featuring automated Wikipedia article ingestion, image caching, and full observability stack integration.

## Tech Stack

- **Backend**: Python, Flask, SQLAlchemy, HTMX
- **Database**: PostgreSQL (StatefulSet)
- **Infrastructure**: Kubernetes (k3d), Docker
- **Automation**: Kubernetes CronJob
- **Configuration**: ConfigMaps, Secrets
- **Storage**: Persistent Volumes


## Features

- **CRUD Todo Management**: Create, read, and list todos with 140-character validation
- **Automated Content Generation**: Hourly CronJob fetches random Wikipedia articles and creates todos
- **Image Caching**: Lorem Picsum images cached with 10-minute TTL to reduce external API calls
- **Request Logging**: Comprehensive logging for monitoring and debugging
- **Kubernetes-Native**: Fully containerized with proper resource management and health checks
- **Observability**: Integrated with Prometheus, Grafana, and Loki (optional)


## Prerequisites

- Docker
- k3d (or any Kubernetes cluster)
- kubectl

## Getting Started

### 1. Create k3d Cluster

```bash
k3d cluster create todo-cluster \
  --port 8081:80@loadbalancer \
  --agents 2
```

### 2. Configure Secrets

Create `manifests/secret.yaml` with your PostgreSQL credentials:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: postgres-secret
  namespace: project
type: Opaque
data:
  POSTGRES_PASSWORD: <base64-encoded-password>
  POSTGRES_DB: <base64-encoded-db-name>
  POSTGRES_URL: <base64-encoded-connection-string>
```

**Encode your values:**
```bash
echo -n "your-password" | base64
echo -n "tododb" | base64
echo -n "postgresql://user:password@postgres-svc:5432/tododb" | base64
```

### 3. Deploy Application

```bash
# Apply shared resources
kubectl apply -f manifests/

# Deploy backend
kubectl apply -f manifests/todo-backend/

# Deploy frontend
kubectl apply -f manifests/todo-app/
```

### 4. Verify Deployment

```bash
# Check all pods are running
kubectl get pods -n project

# Check services
kubectl get svc -n project

# View logs
kubectl logs -n project <pod-name>
```

### 5. Access Application

Open your browser and navigate to:
```
http://localhost:8081/
```

## API Endpoints

### Backend (todo-backend)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/todos` | Retrieve all todos |
| POST | `/todos` | Create new todo (max 140 chars) |

**Example Request:**
```bash
curl -X POST http://localhost:8081/todos \
  -H "Content-Type: application/json" \
  -d '{"text": "Read about Kubernetes on Wikipedia"}'
```

## Project Structure

```
.
├── todo_app/              # Frontend application
├── todo-backend/          # Backend API
└── manifests/            # Kubernetes resources
    ├── todo-app/         # Frontend-specific manifests
    └── todo-backend/     # Backend-specific manifests
```

## Kubernetes Resources

### Core Resources
- **Namespace**: `project` - Isolated environment for the application
- **Ingress**: Routes external traffic to frontend and backend services
- **ConfigMap**: Stores CronJob script for Wikipedia article fetching
- **Secret**: Manages PostgreSQL credentials securely

### Storage
- **PersistentVolume**: Provides storage for database and image cache
- **PersistentVolumeClaim**: Claims storage for StatefulSet
- **StatefulSet**: Runs PostgreSQL with persistent data

### Automation
- **CronJob**: Executes every hour to:
  1. Fetch random Wikipedia article via `Special:Random`
  2. Parse `Location` header for article URL
  3. POST new todo to backend API



