#!/bin/bash
helm ls --all --short -n ricxapp | grep opt | xargs -L1 helm uninstall -n ricxapp
helm ls --all --short -n ricplt | grep e2sim | xargs -L1 helm uninstall -n ricplt
helm ls --all --short -n ricplt | grep e2term | xargs -L1 helm uninstall -n ricplt