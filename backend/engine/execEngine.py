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
            container_id = subprocess.run(['docker', 'run', '-d',
                                           '-v', f'{DOCKER.config["testcases"]}/testcases/:/usr/src/app/testcases',
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
    def run_tests(clientID: str, challenge_name: str, code: str, submit_lang: str) -> str:
        """
        Runs tests in a Docker container and returns the test results.

        Args:
            clientID (str): The ID of the client.
            challenge_name (str): The name of the challenge.
            code (str): The code to be tested.
            submit_lang (str): The language of the submitted code.

        Returns:
            str: The test results.
        """
        if len(DOCKER.containers) == 0:
            DOCKER.refresh_containers()

        container_id = DOCKER.containers[0]
        res = subprocess.run(['docker', 'exec', '-it', '180cfc993f9e5ad616b97509118525847d5aa3bddac59e64c7fb5dc7974a698a', 'python3', 'checker.py', clientID, challenge_name, code, submit_lang], stdout=subprocess.PIPE).stdout.decode().strip()
        print(res)
        return res
        # failed_tests = []
        # for k, v in res.__dict__.items():
        #     if v.status != 'OK':
        #         failed_tests.append(k)
        # if len(failed_tests) > 0:
        #     score = 100% - (len(failed_tests) / len(res.__dict__.keys())) * 100
        #     return f'{score}%', failed_tests
