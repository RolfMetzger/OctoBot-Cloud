from docker.errors import NotFound

from octobot_cloud import docker_client, docker_client_api, ContainerStatus


class Container:
    def __init__(self, name):
        self.name = name

        try:
            self.container = docker_client.containers.get(name)
        except NotFound:
            self.container = None

    def get_container_info(self):
        return docker_client_api.inspect_container(self.container)

    def get_container_port(self, port):
        return docker_client_api.port(self.name, port)

    def get_host_corresponding_port(self, port):
        try:
            return self.get_container_port(port)[0]["HostPort"]
        except TypeError:
            return None

    def is_running(self) -> bool:
        return self.container is not None and self.container.status == ContainerStatus.RUNNING
