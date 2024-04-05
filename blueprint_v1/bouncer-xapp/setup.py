# ==================================================================================
#
#       Copyright (c) 2020 Samsung Electronics Co., Ltd. All Rights Reserved.
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

from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='bouncerxapp',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/LABORA-INF-UFG/openran-br-blueprint/',
    license='Apache 2.0',
    description="Bouncer Python XAPP for O-RAN RIC Platform",
    long_description=read('README.md'),
    author='Daniel Campos',
    author_email='danielcampos@inf.ufg.br',
    python_requires='>=3.8',
    install_requires=["ricxappframe>=3.2.0, <3.3.0"],
    entry_points={"console_scripts": ["run-xapp-entrypoint.py=src.main:launchXapp"]},  # adds a magical entrypoint for Docker
    data_files=[("", ["LICENSE.txt"])],
)

