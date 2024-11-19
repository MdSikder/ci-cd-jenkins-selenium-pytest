pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9'
        VENV_PATH = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                git url: 'https://github.com/MdSikder/ci-cd-jenkins-selenium-pytest.git', branch: 'main'
            }
        }

        stage('Set up Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    apt-get update -y
                    apt-get install -y python3 python3-pip
                    python3 -m pip install --upgrade pip
                    pip install virtualenv
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                echo 'Creating virtual environment...'
                sh '''
                    python3 -m venv ${VENV_PATH}
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    pip install -r requirements.txt || { echo "Dependency installation failed"; exit 1; }
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    pytest --maxfail=1 --disable-warnings -q --html=report.html
                '''
            }
        }

        stage('Upload Test Report') {
            steps {
                echo 'Archiving test report...'
                archiveArtifacts artifacts: 'report.html', allowEmptyArchive: false
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed. Cleaning up...'
            sh 'rm -rf ${VENV_PATH}'
        }
        failure {
            echo 'Build failed. Please check the logs for details.'
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
