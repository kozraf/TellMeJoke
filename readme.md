# TellMeJoke Application 

This repository contains the Kubernetes manifests and associated files for deploying the TellMeJoke application.

## Versions 1.3
### v1.3
- added ingress 

## Introduction

The TellMeJoke application is a lighthearted and fun web application that serves jokes to its users. Designed with scalability and maintainability in mind, the application is divided into three distinct tiers:

- PresentationTier: This is the front-facing part of our application, where users interact and request jokes.
- BusinessTier: This layer handles the business logic, ensuring that the jokes are fetched and delivered correctly.
- DatabaseTier: As the name suggests, this layer is responsible for storing and retrieving jokes.

## Features

- User-Friendly Interface: The application provides a simple and intuitive interface for users to fetch jokes with a single click.
- Scalable Architecture: Designed with a three-tier architecture, each tier can be scaled independently to handle varying loads.
- Responsive: The application is designed to be fast and responsive, delivering jokes quickly to ensure user satisfaction.

## Initial Setup

Before deploying the main components, run the script `tellmejoke_initial_prep_work.sh` to set up necessary directories for the application:

```bash
bash tellmejoke_initial_prep_work.sh
```

**!!Important!!** 
As I am using Ingress - make sure your hosts file can resolve tellmejoke.local to one of the K8 nodes!
**!!Important!!**

## Detailed User Interactions and Data Flow


### User Enters the Website

1. The user enters the URL http://tellmejoke.local:<NodePort> into their browser.
2. The browser sends a request to the IP address associated with tellmejoke.local, which has been mapped to one of the Kubernetes nodes.
3. The request hits the node on the specified NodePort.
4. The NodePort service for the PresentationTier receives this request on the node. This service is set up to listen on a port in the range of 30000-32767.
5. The NodePort service then forwards this request to the appropriate pod running the PresentationTier.
6. The PresentationTier pod, which runs a web server, fetches the index.html file and sends it back through the same path to the user's browser.
7. The user's browser renders the index.html page, displaying the TellMeJoke website.

### User Clicks on "GetJoke"

1. When the user clicks the "GetJoke" button, the embedded JavaScript in index.html sends an HTTP GET request to the BusinessTier on its exposed NodePort.
2. This request first hits the NodePort service of the BusinessTier.
3. The BusinessTier service forwards the request to one of the pods running the business logic.
4. The BusinessTier pod processes this request and needs to fetch a joke from the database. It sends another request to the DatabaseTier.
5. This request is sent to the ClusterIP service of the DatabaseTier, ensuring internal communication within the Kubernetes cluster.
6. The DatabaseTier service forwards the request to the appropriate pod.
7. The DatabaseTier pod fetches a random joke from the database and sends it back to the BusinessTier pod.
8. The BusinessTier pod receives the joke and sends it back to the user's browser through the initial path.
9. The JavaScript on the index.html page then displays the joke to the user.

### User Clicks on "AddJoke"

1. The user enters a joke into a provided text field and clicks the "AddJoke" button.
2. The embedded JavaScript in index.html captures the input and sends an HTTP POST request with the joke data to the BusinessTier on its exposed NodePort.
3. The request reaches the NodePort service of the BusinessTier.
4. The service forwards the joke data to one of the BusinessTier pods.
5. The BusinessTier pod processes the data and sends a request to the DatabaseTier to store the joke.
6. The request to the DatabaseTier is sent to its ClusterIP service.
7. The DatabaseTier service routes the request to the appropriate pod.
8. The DatabaseTier pod processes the request and stores the joke in the database.
9. An acknowledgment is sent back from the DatabaseTier pod to the BusinessTier pod, confirming the joke's storage.
10. The BusinessTier pod then relays this success message back to the user's browser.
11. The user's browser, using the JavaScript on the index.html page, displays a confirmation message to the user, indicating the joke has been added successfully.

## Structure

### DatabaseTier

The `DatabaseTier` provides the backend database for storing jokes. 

#### Files:
- `DatabaseTier-argocd-createapp.yaml`: ArgoCD application definition for the database tier.
- `DatabaseTier-deployment.yaml`: Kubernetes deployment manifest for the database.
- `DatabaseTier-init-job.yaml`: Kubernetes job to initialize the database.
- `DatabaseTier-service.yaml`: Kubernetes service to access the database.
- `Dockerfile`: Dockerfile to build the database container image.
- `init.sql`: SQL script to initialize the database schema.
- `pv.yaml`: Persistent Volume definition for database storage.
- `pvc.yaml`: Persistent Volume Claim definition for the database.

### BusinessTier

The `BusinessTier` provides the backend API for fetching and adding jokes.

#### Files:
- `app.py`: Main application script written in Python 
- `BusinessTier-argocd-createapp.yaml`: ArgoCD application definition for the business tier.
- `BusinessTier-deployment.yaml`: Kubernetes deployment manifest for the business tier.
- `BusinessTier-service.yaml`: Kubernetes service to access the business tier API.
- `Dockerfile`: Dockerfile to build the business tier container image.
- `requirements.txt`: Python dependencies for the business tier.

### PresentationTier

The `PresentationTier` provides the frontend interface for users to interact with the application.

#### Files:
- `Dockerfile`: Dockerfile to build the presentation tier container image.
- `index.html`: Main frontend HTML file.
- `PresentationTier-argocd-createapp.yaml`: ArgoCD application definition for the presentation tier.
- `PresentationTier-deployment.yaml`: Kubernetes deployment manifest for the presentation tier.
- `PresentationTier-service.yaml`: Kubernetes service to access the presentation tier frontend.
- `PresentationTier-ingress-controller.yaml`: Kubernetes ingress controller.

## Deployment

To deploy the application, follow the steps:

1. Ensure ArgoCD is set up and running in your cluster.
2. Apply the ArgoCD application definitions for each tier.
3. Monitor the deployment status using ArgoCD or `kubectl`.

## Technologies Used

- Kubernetes: The entire application is containerized and orchestrated using Kubernetes, ensuring high availability and fault tolerance.
- ArgoCD: Continuous Deployment is managed through ArgoCD, enabling automatic deployments and rollbacks based on Git changes.
- Docker: All tiers of the application are containerized using Docker, ensuring consistency across different environments.
- Python: The BusinessTier is written in Python, leveraging its simplicity and vast libraries.
- MySQL: The DatabaseTier uses MySQL, a reliable and widely-used relational database system.
- NGINX: The PresentationTier uses NGINX to serve the static HTML content.

## Roadmap

- expanding with more basic features
- adding HA
- testing multicloud deployment
- making it more secure

## Contributing

Contributions are welcome. Please submit a pull request or open an issue to discuss changes.
