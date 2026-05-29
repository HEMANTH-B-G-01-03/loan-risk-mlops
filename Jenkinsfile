pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/HEMANTH-B-G-01-03/loan-risk-mlops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t loan-risk-mlops .'
            }
        }

        stage('Stop Existing Container') {
            steps {
                sh 'docker stop loan-risk-app || true'
                sh 'docker rm loan-risk-app || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name loan-risk-app loan-risk-mlops'
            }
        }
    }
}