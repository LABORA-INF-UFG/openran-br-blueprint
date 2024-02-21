#!/bin/bash
kubectl delete deployment e2sim -n ricplt
sudo patch /etc/init.d/swap_off.sh < swap_off.patch
helm install e2sim1 deployer/helm-charts/e2sim-helm/ -n ricplt
patch deployer/helm-charts/e2sim-helm/values.yaml < values.patch
helm install e2sim2 deployer/helm-charts/e2sim-helm/ -n ricplt
