import yaml
import re
import pprint
import json
import os
from kubernetes import client, config
from subprocess import PIPE, run
import time
from flask import Flask,request,json
import urllib.request


app = Flask(__name__)


#Constants
TRIGGER_ALLERT_LOOPING = 'HighRICControlLoopLatency'
TRIGGER_ALLERT_NODE = 'NodeDownAlert'

STATUS_ALLERT = 'firing'


DBAAS_VALUES = 'helm-charts/dbaas/values.yaml'
E2TERM_VALUES = 'helm-charts/e2term/values.yaml'
XAPP_VALUES = 'helm-charts/bouncer-xapp/values.yaml'
E2SIM_VALUES = 'helm-charts/e2sim-helm/values.yaml'

#Globals
optimization_interation= 1

input_1= {"E2Nodes": [
        {"DB": 2,
              "E2Node": 5,
              "E2T": 2,
              "RIC_MAN": 2,
              "SDL": 2,
              "xApp1": 5
        },
        {"DB": 2,
              "E2Node": 2,
              "E2T": 2,
              "RIC_MAN": 2,
              "SDL": 2,
              "xApp1": 2
        },
        {"DB": 2,
              "E2Node": 3,
              "E2T": 2,
              "RIC_MAN": 2,
              "SDL": 2,
              "xApp1": 3
        },
        {"DB": 2,
              "E2Node": 4,
              "E2T": 2,
              "RIC_MAN": 2,
              "SDL": 2,
              "xApp1": 4
        }
    ]
}

input_2= {"E2Nodes": [
        {"DB": 2,
              "E2Node": 5,
              "E2T": 5,
              "RIC_MAN": 2,
              "SDL": 2,
              "xApp1": 5
        },
        {"DB": 2,
              "E2Node": 2,
              "E2T": 2,
              "RIC_MAN": 2,
              "SDL": 2,
              "xApp1": 2
        },
        {"DB": 2,
              "E2Node": 3,
              "E2T": 2,
              "RIC_MAN": 2,
              "SDL": 2,
              "xApp1": 3
        },
        {"DB": 2,
              "E2Node": 4,
              "E2T": 2,
              "RIC_MAN": 2,
              "SDL": 2,
              "xApp1": 4
        }
    ]
}

#A function to read YAML file
#def read_yaml():
#    with open('hwxapp-ns/values.yaml') as file:
#        values = yaml.safe_load(file) 
#    return values

def read_yaml(path):
    with open(path) as file:
        values = yaml.safe_load(file) 
    return values

#A function to update node in YAML file
def update_node_yaml(values,node_name):
    nodeSelector_dict = values['nodeSelector']
    nodeSelector_dict.update({'kubernetes.io/hostname': node_name})
    values.update(nodeSelector_dict)
    values.update({'name': node_name})
    return(values)

#A function to write edited YAML file
#def write_yaml(data):
#    with open('hwxapp-ns/values-edit.yaml', 'w') as file:
#        yaml.dump(data, file)

def write_yaml(data, path_file):
    with open(path_file, 'w') as file:
        yaml.dump(data, file)

#A function to read json result
def read_json():
    with open('test/heuristic_scenario_2.json') as file:
        data = json.load(file) 
    return data

def read_json(it):
    with open(it+'.json') as file:
        data = json.load(file) 
    return data

#A function to read json result
def read_json_1():
    with open('1.json') as file:
        data = json.load(file) 
    return data

#A function to read json result
def read_json_2():
    with open('2.json') as file:
        data = json.load(file) 
    return data

#A function to get db location
def get_db_locations(input):
    nodes_db_list = set([])
    for input_dict in input['E2Nodes']:
        for key in input_dict:
            #print(key)
            #print (input_dict[key])
            if key == 'DB':
                #print ('node'+str(input_dict[key]))
                nodes_db_list.add('node'+str(input_dict[key]))
    #print(nodes_db_list)
    return nodes_db_list

#A function to labels nodes to host DB
def set_nodes_db_location(node_set):
    config.load_kube_config()
    api_instance = client.CoreV1Api()
    body = {
        "metadata": {
            "labels": {
                "node-role.ric.sc/db": "true"}
        }
    }
    node_list = list(node_set)
    node_list_k8s = api_instance.list_node()
    for node_k8s in node_list_k8s.items:
        for node in node_list:
            if node_k8s.metadata.name == node:
                #print("%s\t%s" % (node_k8s.metadata.name, node_k8s.metadata.labels))
                api_response = api_instance.patch_node(node_k8s.metadata.name, body)

#A function to clear labels nodes to host DB
def unset_nodes_db():
    config.load_kube_config()
    api_instance = client.CoreV1Api()
    body = {
        "metadata": {
            "labels": {
                "node-role.ric.sc/db": "None"}
        }
    }
    node_list_k8s = api_instance.list_node()
    for node_k8s in node_list_k8s.items:
        api_response = api_instance.patch_node(node_k8s.metadata.name, body)


#A function to set dbaas replica number in helm
def set_dbaas_replica_number(number_replicas):
    values = read_yaml(DBAAS_VALUES)
    dbaas_values = values['dbaas']
    dbaas_values.update({'saReplicas': number_replicas})
    values['dbaas'] = dbaas_values
    #pprint.pprint(values)
    write_yaml(values, DBAAS_VALUES)

# Method to upgrade dbaas deploy
def upgrade_dbaas_deploy(result):
    #Get db nodes location
    nodes_db_set = get_db_locations(result)
    #Clear db nodes location
    unset_nodes_db()
    #Set db nodes location
    set_nodes_db_location(nodes_db_set)
    #Set db replicas number
    set_dbaas_replica_number(len(nodes_db_set))
    #Upgrade helm r4-dbaas deployment
    os.system('helm upgrade --install r4-dbaas helm-charts/dbaas/ --force -n ricplt')

#A function to get e2term location
def get_e2term_locations(input):
    nodes_e2term_set = set([])
    for input_dict in input['E2Nodes']:
        for key in input_dict:
            #print(key+': '+ str(input_dict[key]))
            if key == 'E2T':
                #print ('node'+str(input_dict[key]))
                nodes_e2term_set.add('node'+str(input_dict[key]))
    #print(nodes_e2term_set)
    return nodes_e2term_set

# Method to remove e2term from nodes from nodes according to the result
def remove_unnecessary_e2_term (result):
    e2term_nodes_installed = run('helm ls --all --short | grep opt-e2term', stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    #print(e2term_nodes_installed.stdout)
    nodes_installed = str(e2term_nodes_installed.stdout).splitlines()
    nodes_tobe_installed = get_e2term_locations(result)
    #print(nodes_installed, nodes_tobe_installed)
    for node_installed in nodes_installed:
        node = str(node_installed).rpartition('-')[2]
        #print(node, node_installed)
        node_uninstall = True
        for node_tobe in nodes_tobe_installed:
            #print(node, node_tobe)
            if node == node_tobe:
                node_uninstall = False
        if node_uninstall:
            os.system('helm uninstall '+node_installed)

# Method to upgrade e2term deploy
def upgrade_e2term_deploy(result):
    remove_unnecessary_e2_term(result)
    nodes_e2term_set = get_e2term_locations(result)
    #os.system('helm ls --all --short | grep opt-e2term | xargs -L1 helm uninstall --wait')
    i = 0 
    for e2term_deploy_node in nodes_e2term_set:
        values = read_yaml(E2TERM_VALUES)
        values['nodeSelector']['kubernetes.io/hostname'] = e2term_deploy_node
        write_yaml(values, E2TERM_VALUES)
        if i == len(nodes_e2term_set) - 1:
            os.system('helm upgrade --install opt'+str(optimization_interation)+'-e2term-'+e2term_deploy_node+' helm-charts/e2term/ -n ricplt --wait')
            i = i+1
        else:
            os.system('helm upgrade --install opt'+str(optimization_interation)+'-e2term-'+e2term_deploy_node+' helm-charts/e2term/ -n ricplt')
            i = i+1
    time.sleep(30)

#A function to get xapp location
def get_xapp_locations(input, xapp_result_id):
    nodes_xapp_set = set([])
    for input_dict in input['E2Nodes']:
        for key in input_dict:
            #print(key+': '+ str(input_dict[key]))
            if key == xapp_result_id:
                #print ('node'+str(input_dict[key]))
                nodes_xapp_set.add('node'+str(input_dict[key]))
    #print(nodes_xapp_set)
    return nodes_xapp_set

# Method to remove xapp from nodes from nodes according to the result
def remove_unnecessary_xapp (result, xapp_result_id):
    xapp_nodes_installed = run('helm ls --all --short | grep opt-'+xapp_result_id.lower(), stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    #print(xapp_nodes_installed.stdout)
    nodes_installed = str(xapp_nodes_installed.stdout).splitlines()
    nodes_tobe_installed = get_xapp_locations(result,xapp_result_id)
    #print(nodes_installed, nodes_tobe_installed)
    for active_deploy in nodes_installed:
        node = str(active_deploy).rpartition('-')[2]
        #print(node, active_deploy)
        node_uninstall = True
        for node_tobe in nodes_tobe_installed:
            #print(node, node_tobe)
            if node == node_tobe:
                node_uninstall = False
        if node_uninstall:
            #print(('helm uninstall '+active_deploy))
            os.system('helm uninstall '+active_deploy)

# Method to upgrade generic xApp deploy
def upgrade_xapp_deploy(input, xapp_name):
    xApp_e2node = get_xApp_e2node(input, xapp_name)
    for xApp_e2node_chain in xApp_e2node:
        values = read_yaml(XAPP_VALUES)
        values['nodeSelector']['kubernetes.io/hostname'] = xApp_e2node_chain[0]
        gNB_str_list = re.split('(\d+)', xApp_e2node_chain[1])
        values['containers'][0]['args']['gNB'] = int(gNB_str_list[1])+optimization_interation*100
        #print(values['nodeSelector']['kubernetes.io/hostname'], values['containers'][0]['args']['gNB'])
        write_yaml(values, XAPP_VALUES)
        os.system('helm upgrade --install opt'+str(optimization_interation)+'-'+xapp_name.lower()+'-'+xApp_e2node_chain[0]+'-e2'+gNB_str_list[1]+' helm-charts/bouncer-xapp/ -n ricxapp')
        #time.sleep(3)
        #print('helm upgrade --install opt-'+xapp_name.lower()+'-'+xApp_e2node_chain[0]+'-e2Node'+gNB_str_list[1]+ ' helm-charts/bouncer-xapp/ -n ricxapp')

    #remove_unnecessary_xapp(input, xapp_name)
    #nodes_xapp_set = get_xapp_locations(input, xapp_name)
    #for xapp_deploy_node in nodes_xapp_set:
    #    values = read_yaml(XAPP_VALUES)
    #    values['nodeSelector']['kubernetes.io/hostname'] = xapp_deploy_node
    #    gNB_str_list = re.split('(\d+)', xApp_e2node[xapp_deploy_node])
    #    values['containers'][0]['args']['gNB'] = gNB_str_list[1]
    #    write_yaml(values, XAPP_VALUES)
    #    os.system('helm upgrade --install opt-'+xapp_name.lower()+'-'+xapp_deploy_node+' helm-charts/bouncer-xapp/ -n ricxapp')




#A function to get E2Nodes location
def get_e2sim_locations(input):
    nodes_e2sim_set = set([])
    for input_dict in input['E2Nodes']:
        for key in input_dict:
            #print(key+': '+ str(input_dict[key]))
            if key == 'E2Node':
                #print ('node'+str(input_dict[key]))
                nodes_e2sim_set.add('node'+str(input_dict[key]))
    return nodes_e2sim_set

#A function to get relation between E2Nodes E2Term
def get_e2node_e2term(input):
    e2node_e2term = {}
    for input_dict in input['E2Nodes']:
        for key in input_dict:
            if key == 'E2Node':
                e2node = ('node'+str(input_dict[key]))
            if key == 'E2T':
                e2term = ('node'+str(input_dict[key]))
        e2node_e2term[e2node] = e2term
    return e2node_e2term

# Method to remove e2sim from nodes from nodes according to the result
def remove_unnecessary_e2sim (input):
    e2sim_nodes_installed = run('helm ls --all --short | grep opt-e2sim', stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    #print(e2sim_nodes_installed.stdout)
    nodes_installed = str(e2sim_nodes_installed.stdout).splitlines()
    nodes_tobe_installed = get_e2sim_locations(input)
    #print(nodes_installed, nodes_tobe_installed)
    for active_deploy in nodes_installed:
        node = str(active_deploy).rpartition('-')[2]
        #print(node, active_deploy)
        node_uninstall = True
        for node_tobe in nodes_tobe_installed:
            #print(node, node_tobe)
            if node == node_tobe:
                node_uninstall = False
        if node_uninstall:
            os.system('helm uninstall '+active_deploy)

# Method to upgrade e2sim deploy
def upgrade_e2sim_deploy(input):
    #remove_unnecessary_e2sim(input)
    nodes_e2sim_set = get_e2sim_locations(input)
    e2term_pods_IPs = get_e2term_pods_IPs()
    e2nodes_e2term = get_e2node_e2term(input)
    for e2sim_deploy_node in nodes_e2sim_set:
        values = read_yaml(E2SIM_VALUES)
        values['nodeSelector']['kubernetes.io/hostname'] = e2sim_deploy_node
        values['image']['args']['e2term'] = e2term_pods_IPs[e2nodes_e2term[e2sim_deploy_node]]
        e2sim_str_list = re.split('(\d+)', e2sim_deploy_node)
        values['image']['args']['id'] = int(e2sim_str_list[1])
        values['image']['args']['gNB'] = int(e2sim_str_list[1])+optimization_interation*100
        write_yaml(values, E2SIM_VALUES)
        os.system('helm upgrade --install opt'+str(optimization_interation)+'-e2sim-'+e2sim_deploy_node+' helm-charts/e2sim-helm/ -n ricplt')



def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

# Method to get e2term POD's IPs
def get_e2term_pods_IPs():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    e2term_pods = {}
    for i in ret.items:
        if ('opt-e2term-node' in i.metadata.name):
            pod_name_list = i.metadata.name.split("-")
            pod_name = pod_name_list[5]
            e2term_pods[pod_name]=i.status.pod_ip
    return e2term_pods

#A function to get relation between xApps E2Node
def get_xApp_e2node(input, xapp_name):
    xApp_e2node = {}
    list_xApp_e2node = []
    for input_dict in input['E2Nodes']:
        for key in input_dict:
            if key == xapp_name:
                xApp = ('node'+str(input_dict[key]))
            if key == 'E2Node':
                e2node = ('node'+str(input_dict[key]))
        xApp_e2node[xApp] = e2node
        list_xApp_e2node.append([xApp,e2node])
        #print (list_xApp_e2node)
    return list_xApp_e2node

#A function to restart RIC and remove optimized VNFs
def restart_RIC_state():
    remove_OPT_VNFs()
    os.system('kubectl rollout restart statefulset statefulset-ricplt-dbaas-server -n ricplt')
    os.system('kubectl rollout restart deployment deployment-ricplt-a1mediator -n ricplt')
    os.system('kubectl rollout restart deployment deployment-ricplt-alarmmanager -n ricplt')
    os.system('kubectl rollout restart deployment deployment-ricplt-appmgr -n ricplt')
    os.system('kubectl rollout restart deployment deployment-ricplt-e2mgr -n ricplt')
    os.system('kubectl rollout restart deployment deployment-ricplt-o1mediator -n ricplt')
    os.system('kubectl rollout restart deployment deployment-ricplt-rtmgr -n ricplt')
    os.system('kubectl rollout restart deployment deployment-ricplt-submgr -n ricplt')
    os.system('kubectl rollout restart deployment deployment-ricplt-vespamgr -n ricplt')
    
#A function to restart RIC and remove optimized VNFs
def remove_OPT_VNFs():
    time.sleep(10)
    e2sim_nodes_installed = run('helm ls --all --short --all-namespaces | grep opt'+str(optimization_interation-1), stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    nodes_installed = str(e2sim_nodes_installed.stdout).splitlines()
    for release in nodes_installed:
        os.system('helm uninstall '+release+' -n ricxapp --wait')
    if optimization_interation == 2:
        for release in nodes_installed:
            os.system('helm uninstall '+release+' -n ricplt --wait')


@app.route('/alert',methods=['POST'])
def alert():
    data = request.json
    pprint.pprint(data)
    for i in data['alerts']:   
        if (i['labels']['alertname'] == TRIGGER_ALLERT_LOOPING and data['status'] == STATUS_ALLERT)\
            or (i['labels']['alertname'] == TRIGGER_ALLERT_NODE and data['status'] == STATUS_ALLERT):
            print('Trigger activated, calling optimization solution')
            run_deployment()
            print('RIC optimization complete')
            return 'RIC environment optimized\n'
    return 'Nothing to do. Untreatable alert\n'
            

@app.route('/')
def hello():
    return 'Webhook for trigger optimization'

def run_deployment():
    global optimization_interation
    if  optimization_interation == 1:
        upgrade_e2sim_deploy(input_1)
        optimization_interation += 1
        upgrade_e2sim_deploy(input_2)
        optimization_interation -= 1
    xapp_name =  'xApp1'
    if  optimization_interation == 1:
        time.sleep(15)
        upgrade_xapp_deploy(input_1, xapp_name)
    if  optimization_interation == 2:
        upgrade_xapp_deploy(input_2, xapp_name)
    remove_OPT_VNFs()
    optimization_interation += 1

if __name__ == '__main__':
    print('Deployer started')
    app.run(debug=True,host='0.0.0.0')
    #run_deployment()
    #(sum_over_time(count by (SIM_ID) (rc_control_loop_latency_seconds > 0.01)[1d:]))


    #Validaded Workflows
    #start_time = time.time()
    #upgrade_dbaas_deploy(input)
    #dbbas_time = time.time()
    #dbbas_duration = dbbas_time - start_time
    #upgrade_e2term_deploy(input)
    #get_e2sim_locations(input)
    #upgrade_e2sim_deploy(input)
    #xapp_name =  'xApp1'
    #upgrade_xapp_deploy(input, xapp_name)
    #e2term_time = time.time()
    #e2term_duration = e2term_time - dbbas_time
    #xapp_name =  'xApp1'
    #xapp_time = time.time()
    #xapp_duration = xapp_time - e2term_time
    #upgrade_e2sim_deploy(input)
    #e2sim_time = time.time()
    #e2sim_duration = e2sim_time - xapp_time
    #final_time = time.time()
    #total_duration = final_time - start_time
    #print(total_duration)
    #df = pd.DataFrame({'dbbas_duration':[dbbas_duration], 'e2term_duration':[e2term_duration], \
    #    'xapp_duration':[xapp_duration], 'e2sim_duration':[e2sim_duration], 'total_duration':[total_duration]})
    #print (df)
