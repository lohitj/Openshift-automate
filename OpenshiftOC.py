#!/usr/local/bin/python
import os
os.system('ls')
services = ['cart-service', 'catalog-service','coolstore-gw'];
os.system("oc login https://master.na39.openshift.opentlc.com --token=Q2NgYjyGPoXhZ8nZXqYXtQrJOTvzQ5qJnC32LwjI00c")
for service in services:
  os.system("oc new-app https://github.com/akilans/ms-node-app.git --strategy=pipeline --name="+service+"-pipeline")
