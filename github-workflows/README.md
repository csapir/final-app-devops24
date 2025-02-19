# GitHub Actions Workflow

The project includes a GitHub Actions workflow for deploying the flask-app to a Kubernetes cluster.

The workflow does the following:

1. Starts a local Kubernetes cluster using Minikube.
2. Installs Helm and deploys the flask-app to the cluster.
3. Runs basic tests on the flask-app's healthcheck endpoint.
4. The workflow is triggered on every push to the `main` branch.

You can check the status and logs of the workflow under the "Actions" tab in GitHub.

