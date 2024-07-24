import cmd
from execEngine import DOCKER

class terminal(cmd.Cmd):
    """
    A command-line interface for interacting with the engine.

    This class provides a set of commands for managing Docker containers.

    Attributes:
        prompt (str): The prompt string displayed to the user.

    Methods:
        do_exit(arg: str) -> None: Exit the terminal.
        do_help(arg: str) -> bool | None: Display help information.
        do_new(arg: str) -> None: Create a new Docker container.
        do_ls(arg: str) -> None: List all available Docker containers.
        do_rm(arg: str) -> None: Remove a Docker container.
        do_echo(arg: str) -> None: Print information about a Docker container.
        do_rebase(arg: str) -> None: Rebase the Docker image.
        do_refresh(arg: str) -> None: Refresh the list of Docker containers.
    """

    prompt = '$/ '

    def do_exit(self, arg: str) -> None:
        """
        Exit the terminal.

        Args:
            arg (str): The command argument.

        Returns:
            None
        """
        return True

    def do_help(self, arg: str) -> bool | None:
        """
        Display help information.

        Args:
            arg (str): The command argument.

        Returns:
            bool or None: The return value from the superclass's do_help method.
        """
        return super().do_help(arg)

    ### Docker Commands ###

    def do_new(self, arg: str) -> None:
        """
        Create a new Docker container.

        Args:
            arg (str): The command argument.

        Returns:
            None
        """
        container = DOCKER.new_container()
        print(f'ContainerID is {container}')

    def do_ls(self, arg: str) -> None:
        """
        List all available Docker containers.

        Args:
            arg (str): The command argument.

        Returns:
            None
        """
        containers = DOCKER.get_containers()
        if len(containers) == 0:
            print('*** No container available ***')
        for i in range(len(containers)):
            print(f'{i+1}) {containers[i]}')

    def do_rm(self, arg: str) -> None:
        """
        Remove a Docker container.

        Args:
            arg (str): The command argument.

        Returns:
            None
        """
        containerID = arg.split()[0]
        if len(containerID) == 0:
            print('*** Missing containerID ***')
        if (DOCKER.remove_container(containerID)):
            print(f'*** removed {containerID} ***')

    def do_echo(self, arg: str) -> None:
        """
        Print information about a Docker container.

        Args:
            arg (str): The command argument.

        Returns:
            None
        """
        id = arg.split()[0]
        name = DOCKER.get_one(id)
        print(f'*** Container with id {id} is {name}***')

    def do_rebase(self, arg: str) -> None:
        """
        Rebase the Docker image.

        Args:
            arg (str): The command argument.

        Returns:
            None
        """
        DOCKER.rebase()

    def do_refresh(self, arg: str) -> None:
        """
        Refresh the list of Docker containers.

        Args:
            arg (str): The command argument.

        Returns:
            None
        """
        DOCKER.refresh_containers()

if __name__ == '__main__':
    terminal().cmdloop()
