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
                    // Create a virtual environment and install dependencies without using sudo
                    sh '''#!/bin/bash
                        # Create the virtual environment
                        python3 -m venv venv

                        # Activate the virtual environment
                        source venv/bin/activate

                        # Install dependencies
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the tests using pytest
                    sh '''#!/bin/bash
                        # Activate the virtual environment
                        source venv/bin/activate

                        # Run tests using pytest
                        pytest tests
                    '''
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
            echo 'Build failed. Please check the logs.'
        }
    }
}
