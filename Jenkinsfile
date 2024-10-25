pipeline {
    agent any
    environment {
        SSH_AGENT_CREDENTIALS = 'ssh_host'
    }
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/nguyenphutu/Docker-Flask-App.git'
            }
        }
        
        stage('SSH to Server') {
            steps {
                sshagent(credentials: [SSH_AGENT_CREDENTIALS]) {
                    sh 'scp -r /var/jenkins_home/workspace/Docker-Flask-App/Dockerfile fuufuu@172.17.0.1:~/repo_git/Docker-Flask-App/'
                    sh 'scp -r /var/jenkins_home/workspace/Docker-Flask-App/app.py fuufuu@172.17.0.1:~/repo_git/Docker-Flask-App/'
                    sh 'scp -r /var/jenkins_home/workspace/Docker-Flask-App/docker-compose.yml fuufuu@172.17.0.1:~/repo_git/Docker-Flask-App/'
                    sh 'scp -r /var/jenkins_home/workspace/Docker-Flask-App/ngrok.yml fuufuu@172.17.0.1:~/repo_git/Docker-Flask-App/'
                    sh 'scp -r /var/jenkins_home/workspace/Docker-Flask-App/requirements.txt fuufuu@172.17.0.1:~/repo_git/Docker-Flask-App/'
                    sh 'ssh fuufuu@172.17.0.1 "cd ~/repo_git/Docker-Flask-App && docker-compose up --build web"'
                }
            }
        }
    }
}
