pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "ishwaryamallesh"   // Your Docker Hub username
        IMAGE_NAME = "todo-list-app"
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
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub',
                        usernameVariable: 'DH_USER',
                        passwordVariable: 'DH_PASS'
                    )
                ]) {
                    sh 'echo $DH_PASS | docker login -u $DH_USER --password-stdin'
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
                sshagent(['EC2_SSH_KEY']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@3.110.128.190 "
                        docker pull ishwaryamallesh/todo-list-app:latest &&
                        docker stop todoapp || true &&
                        docker rm todoapp || true &&
                        docker run -d -p 7000:5000 --name todoapp ishwaryamallesh/todo-list-app:latest
                    "
                    '''
                }
            }
        }
    }
}
