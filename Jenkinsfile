pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'challan'
        CONTAINER_NAME = 'sad_driscoll'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'capstone', url: 'https://github.com/TanyaPat01/Generate-Challan']])
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t $DOCKER_IMAGE_NAME .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run Docker container
                    sh "docker run -d --name $CONTAINER_NAME $DOCKER_IMAGE_NAME"
                }
            }
        }

        stage('View Container Logs') {
            steps {
                script {
                    // View logs of the Docker container
                    sh "docker logs $CONTAINER_NAME"
                }
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    // Add commands for your build and testing steps inside the Docker container
                    // sh 'docker exec $CONTAINER_NAME python3 -m pytest'
                }
            }
        }
    }

    post {
        always {
            // Cleanup: Stop and remove the Docker container after the build
            script {
                sh "docker stop $CONTAINER_NAME || true"
                sh "docker rm $CONTAINER_NAME || true"
            }
        }

        failure {
            emailext (
                subject: "Build Failed: ${currentBuild.fullDisplayName}",
                body: "The build failed 🥺. Please investigate.",
                to: "seleniumadya@gmail.com, adya.tiwari20@st.niituniversity.in, tanya.patel20@st.niituniversity.in, somia.kumari20@st.niituniversity.in"
            )
        }

        success {
            emailext (
                subject: "Build Successful: ${currentBuild.fullDisplayName}",
                body: "Congratulations!!, The build was successful. 🥰",
                to: "seleniumadya@gmail.com, adya.tiwari20@st.niituniversity.in, tanya.patel20@st.niituniversity.in, somia.kumari20@st.niituniversity.in"
            )
        }
    }
}
