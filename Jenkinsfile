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
                export PYTHONPATH=$WORKSPACE
                python -m pip install --break-system-packages -e .
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
                    scp -o StrictHostKeyChecking=no dist/flask_todo-1.0.0-py3-none-any.whl ubuntu@65.1.55.198:~/flaskapp/
                    scp -o StrictHostKeyChecking=no db_create.py ubuntu@65.1.55.198:~/flaskapp/

                    ssh -o StrictHostKeyChecking=no ubuntu@65.1.55.198 << 'EOF'

                    cd ~/flaskapp

                    # 🔧 Install Python if not exists
                    sudo apt update -y
                    sudo apt install -y python3-pip python3-venv

                    # 🔧 Create venv if not exists
                    if [ ! -d "venv" ]; then
                        python3 -m venv venv
                    fi

                    source venv/bin/activate

                    # 🔧 Upgrade pip
                    pip install --upgrade pip

                    # 🔧 Install your app
                    pip install --force-reinstall flask_todo-1.0.0-py3-none-any.whl

                    # 🔧 Run DB setup
                    python db_create.py

                    # 🔥 Kill old app
                    pkill gunicorn || true
                    pkill python || true

                    # 🚀 Run with gunicorn (production way)
                    nohup gunicorn -w 2 -b 0.0.0.0:5000 flask_todo.app:app > app.log 2>&1 &

                    EOF
                    '''
                }
            }
        }
    }
}
