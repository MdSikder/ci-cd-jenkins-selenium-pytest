pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.12'  // Python version, adjust as needed
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo 'Checking out the code from Git repository...'
                checkout scm
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    // Create a virtual environment and install dependencies
                    sh '''#!/bin/bash
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests using pytest
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        sh '''#!/bin/bash
                            source venv/bin/activate
                            pytest tests
                        '''
                    }
                }
            }
        }

        stage('Upload Test Report') {
            steps {
                echo 'Uploading test reports...'
                // Optional: Add steps to upload or store the test report
            }
        }

        stage('Post Actions') {
            steps {
                echo 'Performing post-build actions...'
                // Optional: Add any post actions, like cleanup or notifications
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Optional: Add cleanup steps if needed
        }

        success {
            echo 'Build successful!'
        }

        failure {
            echo 'Build failed, but will continue with next steps.'
        }
    }
}
