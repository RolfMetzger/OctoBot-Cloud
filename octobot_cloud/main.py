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
from logging.config import fileConfig

from octobot_cloud import LOGGING_CONFIG_FILE
from octobot_cloud.app import start_webapp


def main():
    fileConfig(LOGGING_CONFIG_FILE)

    logger = logging.getLogger("OctoBot-Cloud::Main")
    logger.info("starting...")

    start_webapp()


if __name__ == '__main__':
    main()
