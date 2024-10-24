pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '95ab2e87-e19d-4d8a-a1ef-5c4691b10df3', url: 'https://github.com/ShrijithSM/House-Price-Prediction.git']])
            }
        }
        
        stage('build') {
            steps {
                git branch: 'main', credentialsId: '95ab2e87-e19d-4d8a-a1ef-5c4691b10df3', url: 'https://github.com/ShrijithSM/House-Price-Prediction.git'
                sh 'python3 main.py'
            }
        }
        
        stage('test') {
            steps {
                echo "Testing is done"
            }
        }
    }
}