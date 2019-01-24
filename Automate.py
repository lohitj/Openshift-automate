#!/usr/local/bin/python
import os
os.system('ls')
os.system('java -jar jenkins-cli.jar -s https://jenkins-coolstore-cicd-lohit.apps.na39.openshift.opentlc.com/ create-job cart-service < Template.xml')
