#  Drakkar-Software OctoBot-Cloud
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.

import logging
import docker
import flask

from octobot_cloud.cst import *

server_instance = flask.Flask(__name__)

# disable Flask logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.WARNING)

docker_client = docker.from_env()
docker_client_api = docker.APIClient()
