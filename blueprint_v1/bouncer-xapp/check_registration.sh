#!/bin/bash

echo "----------------- Checking if AppMgr is alive -----------------"
curl -X GET http://$(kubectl get pods -n ricplt -o wide | grep appmgr | awk '{print $6}'):8080/ric/v1/health/alive
echo ""
echo "----------------- Checking if AppMgr is ready -----------------"
curl -X GET http://$(kubectl get pods -n ricplt -o wide | grep appmgr | awk '{print $6}'):8080/ric/v1/health/ready
echo ""
echo "----------------- Getting AppMgr Registered xApps -----------------"
curl -X GET http://$(kubectl get pods -n ricplt -o wide | grep appmgr | awk '{print $6}'):8080/ric/v1/xapps