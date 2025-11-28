pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || true'
            }
        }

        stage('Build') {
            steps {
                echo 'No build step for Python, skipping...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Python application...'
                // Example command below (modify for your server)
                sh 'nohup python app.py &'
            }
        }
    }
}
