pipeline {
    agent any

    environment {
        // Optional: Define environment variables here if needed
        PYTHON_VERSION = '3.8'  // Python version, adjust as needed
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
                    // Use bash to create and activate virtual environment, and install dependencies
                    sh '''#!/bin/bash
                        # Create a virtual environment
                        python3 -m venv venv

                        # Activate the virtual environment
                        source venv/bin/activate

                        # Install dependencies from requirements.txt
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the tests inside the virtual environment
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
