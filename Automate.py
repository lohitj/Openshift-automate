#!/usr/local/bin/python
import os
os.system('ls')
services = ['cart-service1', 'catalog-service1','coolstore-gw1'];
for service in services:
	os.system("java -jar jenkins-cli.jar -s https://jenkins-coolstore-cicd-lohit.apps.na39.openshift.opentlc.com/ create-job "+service+" < Template.xml")
	os.system("java -jar jenkins-cli.jar -s https://jenkins-coolstore-cicd-lohit.apps.na39.openshift.opentlc.com/ build "+service)
