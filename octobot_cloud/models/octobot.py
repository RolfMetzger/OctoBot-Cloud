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

import os
from secrets import token_hex

from octobot_cloud import BOTS_FOLDER, CONFIG_FILE, LOGS_FOLDER, TENTACLES_FOLDER, DEFAULT_PORT
from octobot_cloud.models.container import Container
from octobot_cloud.tools.socket_tools import get_open_port


class OctoBot:
    def __init__(self, token=None, port=None):
        self.token = token or token_hex(32)
        self.port = port or get_open_port()
        self.path = self._path()

        if token is None:
            self._create_path()
            self._create_config_file()

        self.ports = self._ports()
        self.volumes = self._volumes()
        self.container = self._container()

    def _create_path(self):
        os.makedirs(self.path)

    def _create_config_file(self):
        open(os.path.join(self.path, CONFIG_FILE), 'a').close()

    def _path(self):
        return os.path.join(os.getcwd(), BOTS_FOLDER, self.token)

    def _ports(self):
        return {f"{DEFAULT_PORT}/tcp": self.port}

    def _volumes(self):
        return {os.path.join(self.path, CONFIG_FILE): {'bind': '/bot/octobot/config.json', 'mode': 'rw'},
                os.path.join(self.path, LOGS_FOLDER): {'bind': '/bot/octobot/logs', 'mode': 'rw'},
                os.path.join(self.path, TENTACLES_FOLDER): {'bind': '/bot/octobot/tentacles', 'mode': 'rw'}}

    def _container(self):
        return Container(self.token)
