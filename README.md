

```markdown
# To-do Web App K8S Cluster

This project sets up a Kubernetes (K8S) cluster to deploy a Python-based to-do web application using Nginx as a reverse proxy.

## Prerequisites

- Docker
- Minikube
- Kubectl
- Git

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Matanmoshes/To-do-web-app-K8S-Cluster.git
cd To-do-web-app-K8S-Cluster
```

### Setup Minikube

Start Minikube:
```bash
minikube start
```

### Deploy the Application

1. **Deploy the To-do App**

Apply the deployment and service for the to-do app:
```bash
kubectl apply -f todo-app-deployment.yaml
kubectl apply -f todo-app-service.yaml
```

2. **Deploy Nginx as Reverse Proxy**

Apply the deployment, config map, and service for Nginx:
```bash
kubectl apply -f nginx-deployment.yaml
kubectl apply -f nginx-configmap.yaml
kubectl apply -f nginx-service.yaml
```

### Accessing the Application

To access the application, find the Minikube IP and the NodePort assigned to the Nginx service:

1. Get the Minikube IP:
```bash
minikube ip
```

2. Get the NodePort for the Nginx service:
```bash
kubectl get svc nginx-service
```

Combine the Minikube IP and NodePort to access the application. For example, if the Minikube IP is `192.168.49.2` and the NodePort is `31274`, open:

```
http://192.168.49.2:31274
```

### Troubleshooting

If you encounter any issues, check the logs of the pods:
```bash
kubectl get pods
kubectl logs <nginx-pod-name>
kubectl logs <todo-app-pod-name>
```

### Git Operations

- To view the remote repository:
```bash
git remote -v
```

- To fetch and merge changes from the remote repository:
```bash
git fetch origin
git merge origin/master
```

- To push changes to the remote repository:
```bash
git push origin master
```



### Acknowledgements

- Kubernetes
- Minikube
- Docker
- Nginx

