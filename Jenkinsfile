pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'your-docker-image-name'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    try {
                        sh 'python -m pytest tests/'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE_NAME .'
                }
            }
        }

        stage('Run Application in Docker') {
            steps {
                script {
                    sh 'docker run -p 8080:8080 $DOCKER_IMAGE_NAME'
                }
            }
        }

        stage('Selenium Test Automation') {
            steps {
                script {
                    // Set up virtual display for headless testing (for Linux)
                    sh 'export DISPLAY=:99'
                    sh 'Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &'

                    // Run Selenium tests
                    sh 'python -m pytest --headless tests/'
                }
            }
        }
    }

    post {
        success {
            echo 'Build and tests passed!'

            // Additional steps for email notification on success
        }

        failure {
            // Send email on failure
            emailext subject: 'Pipeline Failed: ${currentBuild.fullDisplayName}',
                      body: 'The pipeline has failed. Please check the Jenkins console output for details.',
                      to: 'adya.tiwari20@st.niituniversity.in, somia.kumari20@st.niituniversity.in, tanya.patel20@st.niituniversity.in',
                      recipientProviders: [[$class: 'CulpritsRecipientProvider']]
        }
    }
}
