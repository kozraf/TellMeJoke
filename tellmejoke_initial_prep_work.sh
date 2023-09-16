#!/bin/bash

# Initial Preparation Work
# Pull repo from github
sudo git clone -b basic-3tierapp-argocd https://github.com/kozraf/TellMeJoke.git /home/vagrant/RafK8clstr/TellMeJoke

# Create NFS directories for TellMeJoke app
sudo mkdir -p /srv/nfs/k8s/tellmejoke_app-pv
sudo chown nobody:nogroup /srv/nfs/k8s/tellmejoke_app-pv
sudo chmod 777 /srv/nfs/k8s/tellmejoke_app-pv

#Install ingress-controller
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
kubectl create namespace ingress-nginx
helm install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-nginx

# Get the name of the ArgoCD server pod
ARGOCD_SERVER_POD=$(kubectl get pods -n argocd -l app.kubernetes.io/name=argocd-server -o jsonpath='{.items[0].metadata.name}')

# Get default password ArgoCD password - only works if ArgoCD password has not been changed!
ARGOCD_PASSWORD=$(kubectl get secrets -n argocd argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d)

# Use custom ArgoCD password
#ARGOCD_PASSWORD="Password"

# Login to ArgoCD
kubectl exec -n argocd $ARGOCD_SERVER_POD -- argocd login localhost:8080 --insecure --username admin --password $ARGOCD_PASSWORD

#Copy ArgoCD files to ArgoCD pod
kubectl cp /home/vagrant/RafK8clstr/TellMeJoke/DatabaseTier/DatabaseTier-argocd-createapp.yaml argocd/$ARGOCD_SERVER_POD:/tmp/DatabaseTier-argocd-createapp.yaml
kubectl cp /home/vagrant/RafK8clstr/TellMeJoke/BusinessTier/BusinessTier-argocd-createapp.yaml argocd/$ARGOCD_SERVER_POD:/tmp/BusinessTier-argocd-createapp.yaml
kubectl cp /home/vagrant/RafK8clstr/TellMeJoke/PresentationTier/PresentationTier-argocd-createapp.yaml argocd/$ARGOCD_SERVER_POD:/tmp/PresentationTier-argocd-createapp.yaml

# ArgoCD Application Creation
# Use kubectl exec to run argocd CLI commands from within the ArgoCD server pod
kubectl exec -n argocd $ARGOCD_SERVER_POD -- argocd app create --server localhost:8080 --file /tmp/DatabaseTier-argocd-createapp.yaml --insecure
sleep 60
kubectl exec -n argocd $ARGOCD_SERVER_POD -- argocd app create --server localhost:8080 --file /tmp/BusinessTier-argocd-createapp.yaml --insecure
sleep 60
kubectl exec -n argocd $ARGOCD_SERVER_POD -- argocd app create --server localhost:8080 --file /tmp/PresentationTier-argocd-createapp.yaml --insecure

echo "Deployment completed!"