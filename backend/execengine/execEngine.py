import subprocess
from typing import List

class docker:
    """The class manages the code execution logic
    new_container() -> str: Create a new container and return the container ID
    get_containers() -> List[str]: Get all available containers
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
