pipeline {
    agent any
    stages {
        stage("Build") {
            steps {
                sh "docker-compose build"
            }
        }
        stage("Test") {
            steps {
                sh "docker-compose run servicio1 pytest tests/"
            }
        }
        stage("Deploy") {
            steps {
                sh "docker-compose up -d"
            }
        }
    }
}