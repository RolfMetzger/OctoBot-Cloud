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

from octobot_cloud import DEFAULT_SERVER_IP, DEFAULT_SERVER_PORT, server_instance
from octobot_cloud.controllers import load_routes

logger = logging.getLogger("OctoBot-Cloud::App")


def start_webapp():
    logger.info("starting app...")

    logger.info("loading routes")
    load_routes()

    logger.info("started")
    server_instance.run(host=DEFAULT_SERVER_IP,
                        port=DEFAULT_SERVER_PORT,
                        threaded=True)
