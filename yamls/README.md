# Flask App Kubernetes Deployment

## Prerequisites

- Minikube installed
- kubectl configured to use Minikube
- Docker image of the Flask app pushed to Docker Hub (or local registry)
- NGINX Ingress Controller installed on Minikube (for external access)

## Steps to Deploy

1. **Start Minikube:**
   ```bash
   minikube start
   ```

2. **Build and push your Docker image (if not done yet):**
   Build your Docker image with:
   ```bash
   docker build -t yourdockerhubusername/flask-app .
   ```

   Push the image to Docker Hub:
   ```bash
   docker push yourdockerhubusername/flask-app
   ```

3. **Apply the Kubernetes Manifests:**
   Apply the deployment, service, and ingress files:
   ```bash
   kubectl apply -f yamls/deployment.yaml
   kubectl apply -f yamls/service.yaml
   kubectl apply -f yamls/ingress.yaml
   ```

4. **Check if the resources are created successfully:**
   ```bash
   kubectl get pods
   kubectl get services
   kubectl get ingress
   ```

5. **Accessing the Application:**
   Minikube provides an easy way to access the services via a local DNS entry. To get the application URL:
   ```bash
   minikube service flask-app-service
   ```

   Alternatively, if you're using an ingress, you can access the application via the ingress URL:
   ```bash
   minikube tunnel
   ```

   This will provide a direct URL to your app.

6. **Verify the health check:**
   You can verify the health of the app by navigating to:
   ```bash
   http://flask-app.local/healthcheck
   ```

## Troubleshooting

- Ensure that the NGINX Ingress Controller is installed on your Minikube cluster if you are using an ingress.
- Check logs with `kubectl logs <pod-name>` for any errors.
