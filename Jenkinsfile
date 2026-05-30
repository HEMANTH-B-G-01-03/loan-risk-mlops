// pipeline {
//     agent any

//     stages {

//         stage('Clone Repository') {
//             steps {
//                 git branch: 'main',
//                 url: 'https://github.com/HEMANTH-B-G-01-03/loan-risk-mlops.git'
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 sh 'docker build -t loan-risk-mlops .'
//             }
//         }

//         stage('Remove Old Container') {
//             steps {
//                 sh 'docker stop loan-risk-app || true'
//                 sh 'docker rm loan-risk-app || true'
//             }
//         }

//         stage('Deploy Container') {
//             steps {
//                 sh 'docker run -d -p 8000:8000 --name loan-risk-app loan-risk-mlops'
//             }
//         }
//     }
// }


pipeline {
agent any

```
environment {
    IMAGE_NAME = "loan-risk-mlops"
    CONTAINER_NAME = "loan-risk-app"
    PORT = "8000"
}

stages {

    stage('Checkout Source Code') {
        steps {
            echo "Fetching latest source code from GitHub..."
            git branch: 'main',
                url: 'https://github.com/HEMANTH-B-G-01-03/loan-risk-mlops.git'
        }
    }

    stage('Verify Environment') {
        steps {
            echo "Verifying Docker environment..."
            sh 'docker --version'
            sh 'docker ps'
        }
    }

    stage('Build Docker Image') {
        steps {
            echo "Building Docker Image..."
            sh 'docker build -t ${IMAGE_NAME}:latest .'
        }
    }

    stage('Validate Build') {
        steps {
            echo "Docker image built successfully."
            sh 'docker images | grep ${IMAGE_NAME}'
        }
    }

    stage('Remove Old Container') {
        steps {
            echo "Stopping old container if it exists..."
            sh 'docker stop ${CONTAINER_NAME} || true'
            sh 'docker rm ${CONTAINER_NAME} || true'
        }
    }

    stage('Deploy Container') {
        steps {
            echo "Deploying new container..."
            sh '''
            docker run -d \
            --name ${CONTAINER_NAME} \
            -p ${PORT}:${PORT} \
            ${IMAGE_NAME}:latest
            '''
        }
    }

    stage('Health Check') {
        steps {
            echo "Checking application health..."
            sleep(time: 15, unit: 'SECONDS')
            sh 'curl -f http://localhost:${PORT} || exit 1'
        }
    }

    stage('Deployment Summary') {
        steps {
            echo "========================================="
            echo "Loan Risk MLOps Deployment Successful"
            echo "Application Port : ${PORT}"
            echo "Container Name   : ${CONTAINER_NAME}"
            echo "Image Name       : ${IMAGE_NAME}"
            echo "========================================="
        }
    }
}

post {

    success {
        echo "Pipeline completed successfully."
    }

    failure {
        echo "Pipeline failed. Check console logs."
    }

    always {
        echo "Pipeline execution finished."
    }
}
```

}
