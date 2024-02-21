#!/bin/bash

#echo "----------------- Checking the AppMgr Health -----------------"
#curl -H "Content-Type: application/json" -X GET http://$(kubectl get pods -n ricplt -o wide | grep appmgr | awk '{print $6}'):8080/ric/v1/health
#echo ""
echo "----------------- Getting AppMgr Registered xApps -----------------"
curl -H "Content-Type: application/json" -X GET http://$(kubectl get pods -n ricplt -o wide | grep appmgr | awk '{print $6}'):8080/ric/v1/xapps