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

    }

    post {
        success {
            echo '✅ CI Pipeline Completed Successfully'
        }

        failure {
            echo '❌ Pipeline Failed'
        }
    }
}
