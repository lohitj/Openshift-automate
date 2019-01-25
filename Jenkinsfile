node {
   stage("Checkout Source"){
       checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/lohitj/Openshift-automate.git']]])
   }
   stage("Jenkins Way"){
        sh 'python Automate.py'   
   }
   stage("Openshift Way"){
        sh 'python OpenshiftOC.py'   
   }
}
