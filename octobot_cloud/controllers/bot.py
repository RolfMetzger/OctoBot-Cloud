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

from octobot_cloud import server_instance, docker_client, OCTOBOT_OFFICIAL_IMAGE
from octobot_cloud.models.octobot import OctoBot


@server_instance.route("/run")
def run():
    bot = OctoBot()
    docker_client.containers.run(OCTOBOT_OFFICIAL_IMAGE, detach=True, volumes=bot.volumes, name=bot.token)
    return ""


@server_instance.route("/status/<token>")
def status(token):
    bot = OctoBot(token)
    docker_client.containers.run(OCTOBOT_OFFICIAL_IMAGE, detach=True, volumes=bot.volumes, name=bot.token)
    return ""


@server_instance.route("/stop/<token>")
def stop(token):
    bot = OctoBot(token)
    if bot.is_running():
        bot.container.kill()
    return ""
