pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'python -m pip install -r requirements.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'pytest .'
            }
        }
        stage('Code Compliance') {
            steps {
                sh 'pylint helloworld.py'
            }
        }
    }

    post {
        success {
            echo 'Test OK'
        }

        failure {
            echo 'Pipeline failed! Please check the logs.'
        }
    }
}