TellMeJoke version 1.3
3 tiers (Database / Business / Presentation)

Deployed as 3 apps in ArgoCD:
- helm & NFS storage required!
- use git clone to pull TellMeJoke app
- make sure you run 'sudo chmod 700 ./tellmejoke_initial_prep_work.sh' and launch it to prep nfs share for pv.yaml and install ingress_nginx using helm
- - "***-argocd-createapp.yaml" - instruction for ArgoCD how to create an app, which branch to use etc. - copy&paste to ArgoCD "Create App" section
- database-init-job from DatabaseTier my fail when deployed 1st time as highly likely DatabaseTier pod is not ready yet but it will restart complete on 2nd run
