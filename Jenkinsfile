pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the source code from your Git repository
                git branch: 'main', url: 'https://github.com/MdSikder/selenium-pytest-github-ci-cd.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                // Install Python and create a virtual environment
                sh "python3.12 -m venv venv"
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
                    echo "Running tests"
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
