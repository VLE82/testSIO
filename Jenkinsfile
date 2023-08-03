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
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                script {
                    def testResult = sh(script: 'python3 -m pytest .', returnStatus: true)

                    if (testResult == 0) {
                        sh 'git tag -a -f Unit_Tests -m "Passed"'
                        sh 'git push origin Unit_Tests'
                        }
                    else {
                        sh 'git tag -a -f Unit_Tests -m "Failed"'
                        sh 'git push origin Unit_Tests'
            }
                }
            }
        }
        stage('Code Compliance') {
            steps {
                sh 'python3 -m pylint helloworld.py'
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