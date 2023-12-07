pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'capstone'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'capstone', url: 'https://github.com/TanyaPat01/Generate-Challan']])
            }
        }
        
        stage('build') {
            steps {
                git branch:'main', url:'https://github.com/TanyaPat01/Generate-Challan'
                sh 'python3 ops.py'
            }
        }
        
        stage('test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
    }

    post {
        always {
            // This block will always be executed, regardless of the build result
            bat 'docker logout'
        }
        failure {
            emailext(
                attachLog: true,
                body: '''<html>
                        <p>The build failed. Please check the Jenkins console output for details.</p>
                        <p>Build URL: ${BUILD_URL}</p>
                        </html>''',
                subject: 'Build Failure',
                to: 'adyatwr@gmail.com, seleniumadya@gmail.com'
                mimeType: 'text/html'
            )
        }
        success {
            emailext(
                attachLog: true,
                body: 'The build was successful.',
                subject: 'Build Success',
                to: 'adyatwr@gmail.com, seleniumadya@gmail.com'
                mimeType: 'text/html'
            )
        }
    }
}
