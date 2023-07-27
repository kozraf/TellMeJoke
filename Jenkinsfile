pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'docker.io' // docker.io for Docker Hub
        DOCKER_CREDENTIALS_ID = 'docker_hub_login' // The Jenkins credential ID for Docker Hub
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/kozraf/TellMeJoke.git'
            }
        }
        stage('Build and Push Docker Images') {
            steps {
                script {
                    def appOne = docker.build("kozraf/tellmejoke-businesstier:${env.BUILD_NUMBER}", './BusinessTier')
                    def appTwo = docker.build("kozraf/tellmejoke-presentationtier:${env.BUILD_NUMBER}", './PresentationTier')

                    docker.withRegistry("https://${DOCKER_REGISTRY}", "${DOCKER_CREDENTIALS_ID}") {
                        appOne.push()
                        appTwo.push()
                    }
                }
            }
        }
    }
}


