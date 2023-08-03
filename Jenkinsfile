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
                            def lastCommitMessage = sh(script: 'git log -1 --pretty=%B', returnStdout: true).trim()
                            def newCommitMessage = lastCommitMessage + "\n\nUnit Test OK"
                            sh "git commit --amend -m \"${newCommitMessage}\""
                            sh "git pull origin main"
                            sh "git push --force origin HEAD:main"
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