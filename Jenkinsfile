pipeline {
    agent any
    environment {
        SSH_AGENT_CREDENTIALS = 'ssh_host'
        TELEGRAM_TOKEN = '7799067201:AAEOMDltsWiVAzStFDRz3_C-y4JTE0KAiZQ'
        TELEGRAM_CHAT_ID = '-4545546419'
    }
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/nguyenphutu/Docker-Flask-App.git'
            }
        }
		
		stage('Run Tests') {
            steps {
                script {
						sh 'pytest'
                    }
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
                    sh 'ssh fuufuu@172.17.0.1 "cd ~/repo_git/Docker-Flask-App && docker compose build --no-cache --force-rm web"'
                }
            }
        }
    }
    post {
        success {
            script {
                sendTelegramMessage("✅ *Build Successful*\n\n" +
                                    "*Job Name:* ${env.JOB_NAME}\n" +
                                    "*Build Number:* ${env.BUILD_NUMBER}\n" +
                                    "*Branch:* ${env.GIT_BRANCH}\n" +
                                    "*Build URL:* ${env.BUILD_URL}\n" +
                                    "*Duration:* ${currentBuild.durationString}")
            }
        }
        failure {
            script {
                sendTelegramMessage("❌ *Build Failed*\n\n" +
                                    "*Job Name:* ${env.JOB_NAME}\n" +
                                    "*Build Number:* ${env.BUILD_NUMBER}\n" +
                                    "*Branch:* ${env.GIT_BRANCH}\n" +
                                    "*Build URL:* ${env.BUILD_URL}\n" +
                                    "*Duration:* ${currentBuild.durationString}")
            }
        }
    }
}

def sendTelegramMessage(String message) {
    sh """
    curl -s -X POST https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage \\
    -d chat_id=${TELEGRAM_CHAT_ID} \\
    -d text="${message}"
    """
}
