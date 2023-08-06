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
                    def commitHash = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()
                    def testResult = sh(script: 'python3 -m pytest .', returnStatus: true)
                    
                    if (testResult == 0) {
                        sh 'git tag -a -f Unit_Tests_Passed -m "commit ${commitHash}"'
                        sh 'git push --force origin Unit_Tests_Passed'
                        }
                }
            }
        }
        stage('Code Compliance') {
            steps {
                script {
                    def commitHash = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()
                    def pythonFiles = sh(script: 'find . -name "*.py" -not -name "test_*"', returnStdout: true).trim()
                    def pylintResult = sh(script: "python3 -m pylint --fail-under=9 ${pythonFiles}", returnStatus: true)
                    def coverageResult = sh(script: "python3 -m coverage xml test_*.py && python3 -m coverage report", returnStatus: true)

                    if (pylintResult == 0 && coverageResult == 0) {
                        sh 'git tag -a -f Code_Compliance_Passed -m "commit ${commitHash}"'
                        sh 'git push --force origin Code_Compliance_Passed'
                    }

                    step([$class: 'CoberturaPublisher', coberturaReportFile: 'coverage.xml'])
                }
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner';
                    withSonarQubeEnv() {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }
    }
}