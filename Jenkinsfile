pipeline {
    agent any

    environment {
        // Specify Python version
        PYTHON_VERSION = 'python3'
        // Add other environment variables as needed
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                git url: 'https://github.com/tsinghdevops/sample_calculator_flask.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies
                sh """
                ${PYTHON_VERSION} -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                // Run unit tests
                sh """
                source venv/bin/activate
                python -m unittest discover
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                script {
                    def imageName = "your-docker-repo/your-python-app:${env.BUILD_NUMBER}"
                    sh "docker build -t ${imageName} ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    def imageName = "your-docker-repo/your-python-app:${env.BUILD_NUMBER}"
                    withCredentials([string(credentialsId: 'dockerhub-credentials', variable: 'DOCKER_PASSWORD')]) {
                        sh "echo $DOCKER_PASSWORD | docker login -u your-docker-username --password-stdin"
                        sh "docker push ${imageName}"
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // Deploy to Kubernetes (assuming kubectl is configured)
                script {
                    def imageName = "your-docker-repo/your-python-app:${env.BUILD_NUMBER}"
                    sh """
                    kubectl set image deployment/your-deployment your-container=${imageName} --record
                    kubectl rollout status deployment/your-deployment
                    """
                }
            }
        }
    }

    post {
        always {
            // Clean up the workspace
            deleteDir()
        }
        success {
            echo "Deployment successful!"
        }
        failure {
            echo "Deployment failed."
        }
    }
}
