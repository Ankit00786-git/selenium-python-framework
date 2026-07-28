pipeline {
    agent any

    stages {

        stage('Verify Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest tests --html=reports/report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
        }

        success {
            echo 'Build Successful'
        }

        failure {
            echo 'Build Failed'
        }
    }
}
