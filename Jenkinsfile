pipeline {
    agent any

    environment {
        ENV = 'test' // Set default environment to 'test'. Can be overridden by Jenkins parameter.
        PYTHON_VERSION = '3.12'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the source code from your Git repository
                git branch: 'main', url: 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                // Install Python
                sh "python${PYTHON_VERSION} -m venv venv"
                sh ". venv/bin/activate"
                sh "pip install --upgrade pip"
            }
        }

        stage('Install Dependencies') {
            steps {
                // Activate virtual environment and install dependencies
                sh """
                    . venv/bin/activate
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                // Activate virtual environment and run pytest
                sh """
                    . venv/bin/activate
                    echo "Running tests in ${ENV} environment"
                    pytest --maxfail=1 --disable-warnings -q --html=report.html
                """
            }
            post {
                always {
                    // Archive the HTML report as a Jenkins artifact
                    archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
                }
            }
        }
    }

    post {
        always {
            // Cleanup: remove virtual environment
            sh "rm -rf venv"
        }
    }
}
