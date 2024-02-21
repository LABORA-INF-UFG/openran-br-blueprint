FROM python:slim

ENV PYTHONUNBUFFERED=TRUE

#Copy helm binary
COPY copy-files/helm-linux-amd64/helm /usr/local/bin/helm
COPY copy-files/kubectl /usr/local/bin/kubectl
RUN chmod +x /usr/local/bin/kubectl

#Copy Kubernetes authentication file
RUN mkdir /home/.kube
COPY copy-files/config /home/.kube
ENV KUBECONFIG=/home/.kube/config

COPY deployer.py .
COPY deployer-fake.py .
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY helm-charts helm-charts

#ENTRYPOINT ["tail", "-f", "/dev/null"]