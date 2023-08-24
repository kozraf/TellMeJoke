TellMeJoke version 1.0
3 tiers (Database / Business / Presentation)

Deployed as 3 apps in ArgoCD:
"***-argocd-createapp.yaml" - instruction for ArgoCD how to create an app, which branch to use etc. - copy&paste to ArgoCD "Create App" section

database-init-job from DatabaseTier my fail when deployed 1st time as highly likely DatabaseTier pod is not ready yet but it will restart complete on 2nd run
