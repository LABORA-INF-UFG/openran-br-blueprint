#!/bin/bash

namespace="ricxapp"
xapp_name="bouncerxapp"

echo "namespace=$namespace"
echo "xapp_name=$xapp_name"
echo "----------------- Getting pod's logs -----------------"
kubectl logs POD/$(kubectl get pods -n $namespace | grep $namespace-$xapp_name- | awk '{print $1}') -n $namespace
