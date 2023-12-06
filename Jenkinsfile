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
