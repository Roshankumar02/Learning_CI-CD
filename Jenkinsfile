pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Roshankumar02/Learning_CI-CD.git'
            }
        }


        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                python -m pip install --break-system-packages -r requirements.txt
                python -m pip install --break-system-packages pytest build wheel setuptools
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                python -m pytest
                '''
            }
        }

        stage('Build Artifact') {
            steps {
                sh '''
                . venv/bin/activate
                python -m build
                '''
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'dist/*.whl'
            }
        }

    }
}
