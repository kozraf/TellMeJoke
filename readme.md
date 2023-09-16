# TellMeJoke Application 

This repository contains the Kubernetes manifests and associated files for deploying the TellMeJoke application. The application consists of three main components: `DatabaseTier`, `BusinessTier`, and `PresentationTier`.

# Version 1.2.2
- added automation for deployment in ArgoCD as well as Docker images versioning

## Initial Setup

Before deploying the main components, run the script `tellmejoke_initial_prep_work.sh` to set up necessary directories for the application:

```bash
bash tellmejoke_initial_prep_work.sh
```

## DatabaseTier

The `DatabaseTier` provides the backend database for storing jokes. 

### Files:
- `DatabaseTier-argocd-createapp.yaml`: ArgoCD application definition for the database tier.
- `DatabaseTier-deployment.yaml`: Kubernetes deployment manifest for the database.
- `DatabaseTier-init-job.yaml`: Kubernetes job to initialize the database.
- `DatabaseTier-service.yaml`: Kubernetes service to access the database.
- `Dockerfile`: Dockerfile to build the database container image.
- `init.sql`: SQL script to initialize the database schema.
- `pv.yaml`: Persistent Volume definition for database storage.
- `pvc.yaml`: Persistent Volume Claim definition for the database.

## BusinessTier

The `BusinessTier` provides the backend API for fetching and adding jokes.

### Files:
- `app.py`: Main application script.
- `BusinessTier-argocd-createapp.yaml`: ArgoCD application definition for the business tier.
- `BusinessTier-deployment.yaml`: Kubernetes deployment manifest for the business tier.
- `BusinessTier-service.yaml`: Kubernetes service to access the business tier API.
- `Dockerfile`: Dockerfile to build the business tier container image.
- `requirements.txt`: Python dependencies for the business tier.

## PresentationTier

The `PresentationTier` provides the frontend interface for users to interact with the application.

### Files:
- `Dockerfile`: Dockerfile to build the presentation tier container image.
- `index.html`: Main frontend HTML file.
- `PresentationTier-argocd-createapp.yaml`: ArgoCD application definition for the presentation tier.
- `PresentationTier-deployment.yaml`: Kubernetes deployment manifest for the presentation tier.
- `PresentationTier-service.yaml`: Kubernetes service to access the presentation tier frontend.

## Deployment

To deploy the application, follow the steps:

1. Ensure ArgoCD is set up and running in your cluster.
2. Apply the ArgoCD application definitions for each tier.
3. Monitor the deployment status using ArgoCD or `kubectl`.

## Contributing

Contributions are welcome. Please submit a pull request or open an issue to discuss changes.
