import os
import subprocess
from typing import List, Union

class DOCKER:
    """
    A class that represents a Docker container manager.

    Attributes:
        containers (list): A list of container IDs.
        config (dict): A dictionary containing configuration settings for the Docker manager.

    Methods:
        new_container() -> str: Creates a new Docker container and returns its ID.
        get_containers() -> List[str]: Retrieves a list of all Docker container IDs.
        remove_container(container_id: str) -> Union[bool, str]: Stops and removes a Docker container.
        refresh_containers() -> None: Refreshes the list of Docker containers.
        rebase() -> None: Rebuilds the base Docker image.
        run_tests(clientID: str, challenge_name: str, code: str, submit_lang: str) -> str: Runs tests in a Docker container and returns the test results.
    """

    containers = list()
    config = {
        'checker': f'{os.path.abspath(os.path.dirname(__name__))}/checker',
        "lang_ext": {
            'python': 'py',
            'javascript': 'js',
        },
        "checkers": {
            'py': 'python3',
            'js': 'node'
        }
    }

    @staticmethod
    def new_container() -> str:
        """
        Creates a new Docker container and returns its ID.

        Returns:
            str: The ID of the newly created Docker container.
        """
        try:
            # Check if the base:latest image is available
            images = subprocess.run(['docker', 'images', '--format', '{{.Repository}}:{{.Tag}}'], stdout=subprocess.PIPE).stdout.decode().strip()
            if 'base:latest' not in images:
                DOCKER.rebase()

            container_id = subprocess.run(['docker', 'run', '-d',
                                           '-v', f'{DOCKER.config["checker"]}:/usr/src/app/checker',
                                           '-it', 'base:latest'],
                                           stdout=subprocess.PIPE).stdout.decode().strip()[:12]
            DOCKER.containers.append(container_id)
            return container_id
        except Exception as e:
            return str(e)

    @staticmethod
    def get_containers() -> List[str]:
        """
        Retrieves a list of all Docker container IDs.

        Returns:
            List[str]: A list of Docker container IDs.
        """
        try:
            containers = subprocess.run(['docker', 'ps', '-a', '--format', '{{.ID}}'], stdout=subprocess.PIPE).stdout.decode().strip()
            return containers.split('\n')
        except Exception as e:
            return str(e)

    @staticmethod
    def remove_container(container_id: str) -> Union[bool, str]:
        """
        Stops and removes a Docker container.

        Args:
            container_id (str): The ID of the Docker container to remove.

        Returns:
            Union[bool, str]: True if the container was successfully removed, False otherwise.
        """
        try:
            subprocess.run(['docker', 'stop', container_id], stdout=subprocess.PIPE)
            cont = subprocess.run(['docker', 'rm', container_id], stdout=subprocess.PIPE).stdout.decode().strip()
            if cont == container_id:
                DOCKER.containers.remove(container_id)
                return True
            return False
        except Exception as e:
            return str(e)

    @staticmethod
    def refresh_containers() -> None:
        """
        Refreshes the list of Docker containers.
        """
        DOCKER.containers = DOCKER.get_containers()
        if len(DOCKER.containers) == 0:
            DOCKER.new_container
        return

    @staticmethod
    def rebase() -> None:
        """
        Rebuilds the base Docker image.
        """
        try:
            subprocess.run(['docker', 'build', '-t', 'base:latest', '.', '--no-cache'], check=True)
            print('*** Base image recreated successfully ***')
        except subprocess.CalledProcessError as e:
            print(e)
            print('*** Failed to recreate base image ***')
        return

    @staticmethod
    def run_tests(clientID: str, challenge_name: str, code: str, submit_lang: str) -> dict:
        """
        Runs tests in a Docker container and returns the test results.

        Args:
            clientID (str): The ID of the client.
            challenge_name (str): The name of the challenge.
            code (str): The code to be tested.
            submit_lang (str): The language of the submitted code.

        Returns:
            dict: The test results.
        """
        if len(DOCKER.containers) == 0:
            DOCKER.refresh_containers()

        container_id = DOCKER.containers[0]
        res = subprocess.run(['docker', 'exec', '-it', container_id, 'python3', 'checker/checker.py', clientID, challenge_name, code, submit_lang], stdout=subprocess.PIPE).stdout.decode().strip()
        print(res)
        return res
