#!/bin/bash
curl -X POST http://service-deployer.ricinfra.svc.cluster.local/alert -H "Content-Type: application/json" -d @scripts/alert-example.json
#curl -X POST http://127.0.0.1:5000/alert -H "Content-Type: application/json" -d @scripts/alert-example.json