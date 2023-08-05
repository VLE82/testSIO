def commitHash

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
                    commitHash = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()
                    def testResult = sh(script: 'python3 -m pytest .', returnStatus: true)
                    
                    if (testResult == 0) {
                        sh 'git tag -a -f Unit_Tests_Passed -m "commit ${commitHash}"'
                        sh 'git push origin Unit_Tests_Passed'
                        }
                }
            }
        }
        stage('Code Compliance') {
            steps {
                def pythonFiles = sh(script: 'find . -name "*.py"', returnStdout: true).trim()
                def pylintResult = sh(script: "python3 -m pylint --fail-under=9 ${pythonFiles}", returnStatus: true)
        
                if (pylintResult == 0) {
                    sh 'git tag -a -f Code_Compliance_Passed -m "commit ${commitHash}"'
                    sh 'git push origin Code_Compliance_Passed'
                }
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