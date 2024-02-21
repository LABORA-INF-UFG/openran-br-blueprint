################################################################################
#   Copyright (c) 2019 AT&T Intellectual Property.                             #
#                                                                              #
#   Licensed under the Apache License, Version 2.0 (the "License");            #
#   you may not use this file except in compliance with the License.           #
#   You may obtain a copy of the License at                                    #
#                                                                              #
#       http://www.apache.org/licenses/LICENSE-2.0                             #
#                                                                              #
#   Unless required by applicable law or agreed to in writing, software        #
#   distributed under the License is distributed on an "AS IS" BASIS,          #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
#   See the License for the specific language governing permissions and        #
#   limitations under the License.                                             #
################################################################################

{{- define "common.name.e2term" -}}
  {{- printf "e2term" -}}
{{- end -}}

{{- define "common.fullname.e2term" -}}
  {{- $name := ( include "common.name.e2term" . ) -}}
  {{- $namespace := ( include "common.namespace.platform" . ) -}}
  {{- printf "%s-%s" $namespace $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}


{{- define "common.deploymentname.e2term" -}}
  {{- $name := ( include "common.fullname.e2term" . ) -}}
  {{- printf "deployment-%s" $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "common.configmapname.e2term" -}}
  {{- $name := ( include "common.fullname.e2term" . ) -}}
  {{- printf "configmap-%s" $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "common.containername.e2term" -}}
  {{- $name := ( include "common.fullname.e2term" . ) -}}
  {{- printf "container-%s" $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "common.pvname.e2term" -}}
  {{- $name := ( include "common.fullname.e2term" . ) -}}
  {{- printf "pv-%s" $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "common.pvcname.e2term" -}}
  {{- $name := ( include "common.fullname.e2term" . ) -}}
  {{- printf "pvc-%s" $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "common.servicename.e2term.rmr" -}}
  {{- $name := ( include "common.fullname.e2term" . ) -}}
  {{- printf "service-%s-rmr" $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- define "common.servicename.e2term.sctp" -}}
  {{- $name := ( include "common.fullname.e2term" . ) -}}
  {{- printf "service-%s-sctp" $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "common.servicename.e2term.http" -}}
  {{- $name := ( include "common.fullname.e2term" . ) -}}
  {{- printf "service-%s-http" $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "common.servicename.e2term.prometheus" -}}
  {{- $name := ( include "common.fullname.e2term" . ) -}}
  {{- printf "service-%s-prometheus" $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}


{{- define "common.serviceport.e2term.rmr.data" -}}38000{{- end -}}
{{- define "common.serviceport.e2term.rmr.route" -}}4561{{- end -}}
{{- define "common.serviceport.e2term.http" -}}8080{{- end -}}
{{- define "common.serviceport.e2term.sctp" -}}36422{{- end -}}
{{- define "common.serviceport.e2term.prometheus" -}}8088{{- end -}}


{{- define "common.serviceaccountname.e2term" -}}
  {{- $name := ( include "common.fullname.e2term" . ) -}}
  {{- printf "svcacct-%s" $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}


{{- define "common.ingressname.e2term" -}}
  {{- $name := ( include "common.fullname.e2term" . ) -}}
  {{- printf "ingress-%s" $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
