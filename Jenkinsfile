pipeline {
    agent any

    environment {
        // Define any environment variables if needed
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
                // Ensure bash is used for virtual environment setup
                sh 'bash -c "python3 -m venv venv && source venv/bin/activate"'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                // Install any required dependencies (e.g., pytest, selenium)
                sh 'bash -c "source venv/bin/activate && pip install -r requirements.txt"'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // Run the tests inside the virtual environment
                sh 'bash -c "source venv/bin/activate && pytest"'
            }
        }

        stage('Upload Test Report') {
            steps {
                echo 'Uploading test report...'
                // Add your test report upload steps here
            }
        }

        stage('Post Actions') {
            steps {
                echo 'Post actions...'
                // Any post actions you want to perform
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed. Please check the logs.'
        }
    }
}
