from typing import Optional

from docker.errors import NotFound

from octobot_cloud import docker_client


class Container:
    def __init__(self, container):
        self.container = container

    def get_container_info(self):
        return docker_client.inspect_container(self.container)

    def get_container_ports(self):
        return self.get_container_info()['NetworkSettings']['Ports']


def get_container_from_name(name) -> Optional[Container]:
    try:
        return Container(docker_client.containers.get(name))
    except NotFound:
        return None
