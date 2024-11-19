pipeline {
    agent {
        docker {
            // Use an official Python image from Docker Hub
            image 'python:3.8'
            args '-u root' // Ensure root access for container commands if necessary
        }
    }

    environment {
        VENV_DIR = 'venv'  // Directory for virtual environment
        PYTHON = 'python3'  // Python command
        PIP = 'pip3'        // PIP command
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
                echo 'Setting up Python environment...'
                // Create and activate a virtual environment
                sh """
                    $PYTHON -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    $PIP install --upgrade pip
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing required dependencies...'
                // Install dependencies from requirements.txt
                sh """
                    source $VENV_DIR/bin/activate
                    if [ -f requirements.txt ]; then
                        $PIP install -r requirements.txt
                    fi
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // Run your test suite (assuming pytest)
                sh """
                    source $VENV_DIR/bin/activate
                    pytest --maxfail=5 --disable-warnings -q
                """
            }
        }

        stage('Upload Test Report') {
            steps {
                echo 'Uploading test report...'
                // Example: Copy test reports to a specific directory for further processing
                sh """
                    source $VENV_DIR/bin/activate
                    mkdir -p reports
                    cp test_report.xml reports/
                """
            }
        }

        stage('Post Actions') {
            steps {
                echo 'Cleaning up...'
                // Clean up the virtual environment
                sh 'rm -rf $VENV_DIR'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Build completed successfully.'
        }
        failure {
            echo 'Build failed. Please check the logs.'
        }
    }
}
