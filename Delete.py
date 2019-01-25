#!/usr/local/bin/python
import os
os.system('ls')
services = ['cart-service', 'catalog-service','coolstore-gw'];
for service in services:
	os.system("java -jar jenkins-cli.jar -s https://jenkins-coolstore-cicd-lohit.apps.na39.openshift.opentlc.com/ delete-job "+service)
