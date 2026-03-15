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
                pip install --break-system-packages -e .
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
        stage('Deploy') {
            steps {
                sshagent(['ec2-key']) {
                    sh '''
                    scp -o StrictHostKeyChecking=no dist/*.whl ubuntu@65.1.55.198:~/flaskapp/
                    
                    ssh -o StrictHostKeyChecking=no ubuntu@65.1.55.198 << EOF
                    cd flaskapp
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install *.whl
                    pkill gunicorn || true
                    nohup gunicorn -w 4 app:app -b 0.0.0.0:8000 &
                    EOF
                    '''
                }
            }
        }


    }
}
