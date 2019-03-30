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

PROJECT_NAME = "octobot_cloud"
VERSION = "1.0.0"

# docker
OCTOBOT_OFFICIAL_IMAGE = "drakkarsoftware/octobot"

# OctoBot
CONFIG_FILE = "config.json"
LOGS_FOLDER = "logs"
TENTACLES_FOLDER = "tentacles"
DEFAULT_PORT = 5001

# OctoBot-Cloud
BOTS_FOLDER = "bots"
LOGGING_CONFIG_FILE = f"{LOGS_FOLDER}/logging_config.ini"

# App
DEFAULT_SERVER_IP = 'localhost'
DEFAULT_SERVER_PORT = 8080
