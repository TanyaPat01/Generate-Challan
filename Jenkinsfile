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
        failure {
            emailext (
                subject: "Build Failed: ${currentBuild.fullDisplayName}",
                body: "The build failed. Please investigate.",
                to: "seleniumadya@gmail.com, adya.tiwari20@st.niituniversity.in, tanya.patel20@st.niituniversity.in, somia.kumari20@st.niituniversity.in"
            )
        }
        success {
            emailext (
                subject: "Build Successful: ${currentBuild.fullDisplayName}",
                body: "The build was successful.",
                to: "seleniumadya@gmail.com, adya.tiwari20@st.niituniversity.in, tanya.patel20@st.niituniversity.in, somia.kumari20@st.niituniversity.in"
            )
        }
    }

}
