#!/usr/local/bin/python
import os
os.system('ls')
services = ['cart-service', 'catalog-service','coolstore-gw','inventory-service','pricing-service','rating-service','review-service','sso-service'];
os.system("oc login https://master.na39.openshift.opentlc.com --token=gA8ocw_icOIsFybOUvinkoy0EIaaTouuOu6AxuExLp8")
for service in services:
  os.system("oc new-app https://github.com/akilans/ms-node-app.git --strategy=pipeline --name="+service+"-pipeline")
