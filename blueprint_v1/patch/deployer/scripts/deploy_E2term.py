from kubernetes import client, config
import os
import yaml
import time

E2TERM_VALUES = 'helm-charts/e2term/values.yaml'

def read_yaml(path):
    with open(path) as file:
        values = yaml.safe_load(file) 
    return values

def write_yaml(data, path_file):
    with open(path_file, 'w') as file:
        yaml.dump(data, file)


def main():
    config.load_kube_config()

    api_instance = client.CoreV1Api()

    body = {
        "metadata": {
            "labels": {
                "beta.kubernetes.io/arch":"amd64"
                }
        }
    }
    node_list = api_instance.list_node()
    values = read_yaml(E2TERM_VALUES)
    i = 1 
    for node in node_list.items:
        if node.metadata.name != 'node1':
            values = read_yaml(E2TERM_VALUES)
            values['nodeSelector']['kubernetes.io/hostname'] = node.metadata.name
            write_yaml(values, E2TERM_VALUES)
            if i == len(node_list.items) - 1:
                os.system('helm upgrade --install opt-e2term-'+node.metadata.name+' helm-charts/e2term/ -n ricplt --wait')
                #print('helm upgrade --install opt-e2term-'+node.metadata.name+' helm-charts/e2term/ -n ricplt --wait')
                i = i+1
            else:
                os.system('helm upgrade --install opt-e2term-'+node.metadata.name+' helm-charts/e2term/ -n ricplt')
                #print('helm upgrade --install opt-e2term-'+node.metadata.name+' helm-charts/e2term/ -n ricplt')
                i = i+1
    time.sleep(30)


if __name__ == '__main__':
    main()