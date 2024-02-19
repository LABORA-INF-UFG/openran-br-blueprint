#!/bin/bash

echo "----------------- Getting AppMgr Registered xApps -----------------"
curl -H "Content-Type: application/json" http://$(kubectl get pods -n ricplt -o wide | grep appmgr | awk '{print $6}'):8080/ric/v1/xapps