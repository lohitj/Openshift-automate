#!/usr/local/bin/python
import os
os.system('ls')
services = ['cart-service', 'catalog-service','coolstore-gw','inventory-service','pricing-service','rating-service','review-service','sso-service'];
for service in services
	os.system('java -jar jenkins-cli.jar -s https://jenkins-coolstore-cicd-lohit.apps.na39.openshift.opentlc.com/ create-job "+service" < Template.xml")
