pipeline {
    agent any
    parameters {
    choice(
        name: 'BROWSER',
        choices: ['chrome', 'firefox', 'edge'],
        description: 'Select Browser'
    )

    choice(
        name: 'ENV',
        choices: ['DEV', 'QA', 'UAT'],
        description: 'Select Environment'
    )

    booleanParam(
        name: 'HEADLESS',
        defaultValue: true,
        description: 'Run tests in headless mode'
    )
}
    stages {

        stage('Verify Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                rm -rf venv
                python3 -m venv venv
                ls -la venv/bin
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
    }
}
