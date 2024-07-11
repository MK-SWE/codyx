import subprocess
from typing import List, Union

class docker:
    """The class manages the code execution logic
    new_container() -> str: Create a new container and return the container ID
    get_containers() -> List[str]: Get all available containers
    remove_container(container_id: str) -> Union[bool, str]: Remove a container by ID
    """
    containers = set()

    @staticmethod
    def new_container() -> str:
        """Create a new container
            @Returns: str represent the container ID
        """
        try:
            container_id = subprocess.run(['docker', 'run', '-d', '-it', 'base:latest'], stdout=subprocess.PIPE).stdout.decode().strip()[:12]
            docker.containers.add(container_id)
            return container_id
        except Exception as e:
            return str(e)

    @staticmethod
    def get_containers() -> List[str]:
        """Get all available containers
            @Returns: List[str] represent the container ID
        """
        try:
            containers = subprocess.run(['docker', 'ps', '-a', '--format', '{{.ID}}'], stdout=subprocess.PIPE).stdout.decode().strip()
            return containers.split('\n')
        except Exception as e:
            return str(e)

    @staticmethod
    def remove_container(container_id: str) -> Union[bool, str]:
        """Remove a container
            @Params: container_id: str represent the container ID
            @Returns: bool represent the success of the operation
        """
        try:
            subprocess.run(['docker', 'stop', container_id], stdout=subprocess.PIPE)
            cont = subprocess.run(['docker', 'rm', container_id], stdout=subprocess.PIPE).stdout.decode().strip()
            if cont == container_id:
                docker.containers.remove(container_id)
                return True
            return False
        except Exception as e:
            return str(e)
