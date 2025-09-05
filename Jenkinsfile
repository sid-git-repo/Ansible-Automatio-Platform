
pipeline {
  agent any

  options {
    timestamps()
    ansiColor('xterm')
  }

  tools {
    python 'Python3'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Setup venv') {
      steps {
        sh '''
        python -m venv .venv
        . .venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt -r requirements-dev.txt
        '''
      }
    }
    stage('Lint') {
      steps {
        sh '. .venv/bin/activate && make lint'
      }
    }
    stage('Unit & Molecule Tests') {
      steps {
        sh '. .venv/bin/activate && make molecule || true'
      }
    }
    stage('Package') {
      steps {
        sh 'tar czf artifact.tar.gz playbooks roles inventories library filter_plugins'
        archiveArtifacts artifacts: 'artifact.tar.gz', fingerprint: true
      }
    }
  }
  post {
    always {
      junit allowEmptyResults: true, testResults: '**/molecule/**/junit.xml'
    }
  }
}
