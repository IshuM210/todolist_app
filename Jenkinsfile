pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "ishwaryamallesh"   // Your Docker Hub username
        IMAGE_NAME = "todo-list-app"              // Image name
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t $DOCKERHUB_USER/$IMAGE_NAME:latest .
                """
            }
        }
        stage('Docker Hub Login') {
        steps {
            withCredentials([usernamePassword(credentialsId: 'dockerhub', 
                                         usernameVariable: 'DOCKERHUB_USER', 
                                         passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                sh 'echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USER --password-stdin'
        }
             }
        }

        stage('Push to Docker Hub') {
            steps {
                sh """
                docker push $DOCKERHUB_USER/$IMAGE_NAME:latest
                """
            }
        }

        stage('Deploy to EC2') {
            steps {
                sh """
                ssh -o StrictHostKeyChecking=no ubuntu@3.110.33.101 '
                    docker pull $DOCKERHUB_USER/$IMAGE_NAME:latest
                    docker stop todoapp || true
                    docker rm todoapp || true
                    docker run -d -p 7000:5000 --name todoapp $DOCKERHUB_USER/$IMAGE_NAME:latest
                '
                """
            }
        }
    }
}
