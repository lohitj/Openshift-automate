#!/usr/local/bin/python
import os
os.system('ls')
print("wget http://jenkins-cicd-test.apps.na39.openshift.opentlc.com/jnlpJars/jenkins-cli.jar")
print("java -jar jenkins-cli.jar -s https://jenkins-coolstore-cicd-lohit.apps.na39.openshift.opentlc.com/ create-job cart-service < Template.xml")
