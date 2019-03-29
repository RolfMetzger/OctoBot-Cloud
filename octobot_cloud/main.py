import os
from secrets import token_hex

import docker

from octobot_cloud import OCTOBOT_OFFICIAL_IMAGE, CONFIG_FILE, LOGS_FOLDER, TENTACLES_FOLDER, BOTS_FOLDER


def main():
    client = docker.from_env()

    # setup bot
    bot_id = token_hex(32)
    pwd = os.path.join(os.getcwd(), BOTS_FOLDER, bot_id)
    os.makedirs(pwd)

    # prevent config file not exists
    open(os.path.join(pwd, CONFIG_FILE), 'a').close()

    volumes = {os.path.join(pwd, CONFIG_FILE): {'bind': '/bot/octobot/config.json', 'mode': 'rw'},
               os.path.join(pwd, LOGS_FOLDER): {'bind': '/bot/octobot/logs', 'mode': 'rw'},
               os.path.join(pwd, TENTACLES_FOLDER): {'bind': '/bot/octobot/tentacles', 'mode': 'rw'}}

    # client.images.pull("ubuntu", tag="latest")
    client.containers.run(OCTOBOT_OFFICIAL_IMAGE, detach=True, volumes=volumes, name=bot_id)


if __name__ == '__main__':
    main()
