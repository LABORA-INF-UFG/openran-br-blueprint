# ==================================================================================
#   Copyright (c) 2020 Samsung Electronics Co., Ltd. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# ==================================================================================
FROM alpine:3.11 as bldr

ARG rmr_version=4.8.0

RUN apk update && apk add autoconf automake build-base cmake libtool pkgconfig git sudo
RUN git clone --branch $rmr_version https://gerrit.oran-osc.org/r/ric-plt/lib/rmr \
    && cd rmr \
    && mkdir .build; cd .build \
    && echo "<<<installing rmr devel headers>>>" \
    && cmake .. -DDEV_PKG=1; make install \
    && echo "<<< installing rmr .so>>>" \
    && cmake .. -DDEV_PKG=0; make install

FROM python:3.8-alpine

ARG frame_version=3.2.0

COPY --from=bldr /usr/local/bin/rmr* /usr/local/bin/
COPY --from=bldr /usr/local/include/rmr /usr/local/include/rmr
COPY --from=bldr /usr/local/lib64/librmr* /usr/local/lib64/

ENV LD_LIBRARY_PATH=/usr/local/lib/:/usr/local/lib64

# sdl needs gcc
RUN apk update && apk add gcc musl-dev bash git

# RMR setup
RUN mkdir -p /opt/route/
COPY init/routes.rt /opt/route/routes.rt
ENV RMR_SEED_RT=/opt/route/routes.rt
ENV RMR_LOG_VLEVEL=4

RUN git clone -b ${frame_version} https://github.com/o-ran-sc/ric-plt-xapp-frame-py /ric-plt-xapp-frame-py/
RUN pip install --upgrade pip && pip install certifi six python_dateutil setuptools urllib3 logger requests inotify_simple mdclogpy google-api-python-client msgpack ricsdl pycrate
RUN touch /ric-plt-xapp-frame-py/ricxappframe/entities/__init__.py && touch /ric-plt-xapp-frame-py/ricxappframe/entities/rnib/__init__.py
RUN pip install /ric-plt-xapp-frame-py/

# Install
COPY setup.py /tmp
COPY README.md /tmp
COPY LICENSE.txt /tmp/
COPY src/ /tmp/src
COPY init/ /tmp/init
RUN pip install /tmp

ENV PYTHONUNBUFFERED=1

# Set up ConfigMap
RUN mkdir -p /opt/ric/config && chmod -R 755 /opt/ric/config
COPY init/ /opt/ric/config
ENV CONFIG_FILE=/opt/ric/config/config-file.json

# For Default DB connection, modify for resp kubernetes env
ENV DBAAS_SERVICE_PORT=6379
ENV DBAAS_SERVICE_HOST=service-ricplt-dbaas-tcp.ricplt.svc.cluster.local

# Run xApp (command set on setup.py file)
CMD run-xapp-entrypoint.py
