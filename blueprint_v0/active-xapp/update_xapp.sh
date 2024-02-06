#!/bin/bash

namespace="ricxapp"
xapp_name="activexapp"

echo "namespace=$namespace"
echo "xapp_name=$xapp_name"

echo "----------------- Onboarding the xApp chart -----------------"
dms_cli onboard init/config-file.json init/schema.json

echo "----------------- Terminating xApp pod -----------------"
dms_cli uninstall $xapp_name $namespace

echo -n "Waiting pod termination"
while kubectl get pods -n $namespace | grep -q $namespace-$xapp_name-
do
    sleep 1 # seconds
    echo -n "."
done

printf "\n"
echo "----------------- Removing previous image -----------------"
docker image rm 127.0.0.1:5001/$xapp_name:1.0.0

echo "----------------- Building new image -----------------"
docker build . -t 127.0.0.1:5001/$xapp_name:1.0.0 --network host

echo "----------------- Pushing new image -----------------"
docker push 127.0.0.1:5001/$xapp_name:1.0.0

echo "----------------- Installing the xApp -----------------"
dms_cli install $xapp_name 1.0.0 $namespace

echo -n "Waiting pod creation"
while ! kubectl get pods -n $namespace | grep $namespace-$xapp_name- | grep -q "1/1";
do
    if kubectl get pods -n $namespace | grep $namespace-$xapp_name- | grep -q CrashLoopBackOff; then 
        printf "\n%s" "INSTALLATION ERROR: CrashLoopBackOff"
        break
    fi
    sleep 1 # seconds
    echo -n .
done

printf "\n"

echo "----------------- Getting pod's logs -----------------"
sleep 1
kubectl logs POD/$(kubectl get pods -n $namespace | grep $namespace-$xapp_name- | awk '{print $1}') -n $namespace | tail -n 3