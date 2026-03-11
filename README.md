# Kubernetes Learning Projects

Production-ready Kubernetes applications demonstrating cloud-native development patterns, microservices architecture, and DevOps practices.

---

## Projects

### 1. Distributed Microservices System
Multi-container pod architecture with inter-service HTTP communication, PostgreSQL persistence, and full observability stack integration.

**Tech Stack:** Kubernetes, Flask, PostgreSQL, Prometheus, Grafana, Loki  
**Key Concepts:** Multi-container pods, StatefulSets, ConfigMaps, Secrets, service discovery

[View detailed documentation for log output →](./log_output/README.md)
[PingPong->](./pingpong/README.md)

---

### 2. [Cloud-Native Todo Application](./project_app/)
Full-stack CRUD application with automated Wikipedia content generation via CronJobs, image caching, and database persistence.

**Tech Stack:** Kubernetes, Flask, PostgreSQL, CronJobs, Persistent Volumes  
**Key Concepts:** StatefulSets, CronJob scheduling, namespace isolation, twelve-factor app

[View detailed documentation →](./project_app/README.md)

---

## Quick Start

Each project has detailed setup instructions in its documentation. Both run on k3d clusters with similar configuration.
```bash
# Create k3d cluster
k3d cluster create --port 8081:80@loadbalancer --agents 2

# Deploy microservices system
kubectl apply -f manifests/
kubectl apply -f log_output/manifests/
kubectl apply -f pingpong/manifests/

# OR deploy todo application
kubectl apply -f project_app/manifests/
```



## Future Improvements

- [ ] Add CI/CD pipeline with GitHub Actions
- [ ] Implement resource limiting and health checks
- [ ] Implement Terraform for infrastructure as code
- [ ] Add Helm chart for easier deployment
- [ ] Implement horizontal pod autoscaling
- [ ] Add integration tests
- [ ] Add rate limiting to APIs
- [ ] Deploy on cloud infrastructure

## License

This project is part of a Kubernetes learning exercise.