# ExecEngine -->

This Python module provides a class `DOCKER` that manages Docker containers. It allows you to create, retrieve, remove Docker containers, refresh the list of containers, rebuild the base Docker image, and run tests in a Docker container.

## Class Attributes

- `containers`: A list that stores the IDs of Docker containers.
- `config`: A dictionary that contains configuration settings for the Docker manager.

## Class Methods

### `new_container() -> str`

This method creates a new Docker container and returns its ID. If an error occurs during the creation of the Docker container, it returns the error message as a string.

### `get_containers() -> List[str]`

This method retrieves a list of all Docker container IDs. If an error occurs during the retrieval of Docker container IDs, it returns the error message as a string.

### `remove_container(container_id: str) -> Union[bool, str]`

This method stops and removes a Docker container. It takes the ID of the Docker container to remove as an argument. If the Docker container is successfully removed, it returns `True`. If the Docker container cannot be removed, it returns `False`. If an error occurs during the removal of the Docker container, it returns the error message as a string.

### `refresh_containers() -> None`

This method refreshes the list of Docker containers. It does not return any value.

### `rebase() -> None`

This method rebuilds the base Docker image. It does not return any value. If an error occurs during the rebuilding of the base Docker image, it prints the error message.

### `run_tests(clientID: str, challenge_name: str, code: str, submit_lang: str) -> str`

This method runs tests in a Docker container and returns the test results. It takes the following arguments:

- `clientID`: The ID of the client.
- `challenge_name`: The name of the challenge.
- `code`: The code to be tested.
- `submit_lang`: The language of the submitted code.

If an error occurs during the execution of tests, it returns the error message as a string.

## Usage

To use this module, you need to import it in your Python script as follows:

```python
import execEngine
```

Then, you can create an instance of the `DOCKER` class and call its methods. For example, to create a new Docker container, you can do:

```python
docker_manager = execEngine.DOCKER
container_id = docker_manager.new_container()
```

## Dependencies

This module uses the following Python libraries:

- `os`
- `subprocess`
- `typing`

It also requires Docker to be installed on the system.


# The execEngine CMD Module

This Python module provides a command-line interface for interacting with the Docker engine. It uses the `DOCKER` class from the `execEngine` module to manage Docker containers.

## Class Attributes

- `prompt`: A string that represents the prompt displayed to the user.

## Class Methods

### `do_exit(arg: str) -> None`

This method exits the terminal. It takes the command argument as an argument and does not return any value.

### `do_help(arg: str) -> bool | None`

This method displays help information. It takes the command argument as an argument and returns the return value from the superclass's `do_help` method.

### `do_new(arg: str) -> None`

This method creates a new Docker container. It takes the command argument as an argument and does not return any value.

### `do_ls(arg: str) -> None`

This method lists all available Docker containers. It takes the command argument as an argument and does not return any value.

### `do_rm(arg: str) -> None`

This method removes a Docker container. It takes the command argument as an argument and does not return any value.

### `do_echo(arg: str) -> None`

This method prints information about a Docker container. It takes the command argument as an argument and does not return any value.

### `do_rebase(arg: str) -> None`

This method rebases the Docker image. It takes the command argument as an argument and does not return any value.

### `do_refresh(arg: str) -> None`

This method refreshes the list of Docker containers. It takes the command argument as an argument and does not return any value.

## Usage

To use this module, you need to import it in your Python script as follows:

```python
import terminal
```

Then, you can create an instance of the `terminal` class and call its methods. For example, to create a new Docker container, you can do:

```python
terminal_instance = terminal.terminal()
terminal_instance.do_new()
```

## Dependencies

This module uses the following Python libraries:

- `cmd`
- `execEngine`

## License

This project is licensed under the MIT License.
