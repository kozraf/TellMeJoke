# Create NFS directories for TellMeJoke app
sudo mkdir -p /srv/nfs/k8s/tellmejoke_app-pv
sudo chown nobody:nogroup /srv/nfs/k8s/tellmejoke_app-pv
sudo chmod 777 /srv/nfs/k8s/tellmejoke_app-pv