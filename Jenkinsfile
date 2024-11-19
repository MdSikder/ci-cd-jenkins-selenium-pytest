pipeline {
    agent { label 'linux' }

    environment {
        PYTHON_VERSION = '3.9'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the latest code from the provided Git repository
                git 'https://github.com/MdSikder/ci-cd-jenkins-selenium-pytest.git'
            }
        }

        stage('Set up Python') {
            steps {
                // Set up Python environment
                sh 'sudo apt-get update'
                sh 'sudo apt-get install python3 python3-pip'
                sh "python3 -m pip install --upgrade pip"
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install the dependencies from requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests with pytest and generate an HTML report
                sh 'pytest --maxfail=1 --disable-warnings -q --html=report.html'
            }
        }

        stage('Upload Test Report') {
            steps {
                // Archive the test report as a build artifact
                archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            }
        }
    }
}
