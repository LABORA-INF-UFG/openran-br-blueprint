#!/bin/bash

namespace="ricxapp"
xapp_name="reactivexapp"
n_rows_log=5

echo "namespace=$namespace"
echo "xapp_name=$xapp_name"
echo "----------------- Getting pod's logs -----------------"
while true;
do
    output=$(kubectl logs POD/$(kubectl get pods -n $namespace | grep $namespace-$xapp_name- | awk '{print $1}') -n $namespace | tail -n $n_rows_log)
    clear
    echo "$output"
    sleep 1
done