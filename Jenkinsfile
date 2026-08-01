pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning Flask Application Code'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python Dependencies'
                sh '''
                python3 --version
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Application Test'
                sh '''
                python3 -c "import app; print('Flask app import successful')"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image'
                sh '''
                docker build -t project5-flask-app .
                '''
            }
        }

        stage('Deploy Flask Container') {
            steps {
                echo 'Deploying Flask Application'

                sh '''
                docker stop project5-flask-container || true
                docker rm project5-flask-container || true

                docker run -d \
                --name project5-flask-container \
                -p 5000:5000 \
                project5-flask-app
                '''
            }
        }
    }

    post {

        success {
            echo '✅ CI/CD Pipeline Completed Successfully'
        }

        failure {
            echo '❌ Pipeline Failed'
        }
    }
}
