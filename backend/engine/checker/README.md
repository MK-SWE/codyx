# Checker

This Python module provides a function `checker` that executes a code submission for a given challenge and language.

## Function

### `checker() -> None`

This function retrieves the client ID, challenge name, code, and language from command-line arguments. It then copies the corresponding test cases file to a directory named after the client ID. After decoding the escape sequences in the code, it writes the decoded code to a file named 'submit.{lang}' in the client ID directory. It then executes the checker for the submitted code using the appropriate interpreter, prints the result of the checker, and removes the client ID directory. This function does not return any value.

## Usage

To use this module, you need to import it in your Python script as follows:

```python
import checker
```

Then, you can call the `checker` function. For example:

```python
checker.checker()
```

## Dependencies

This module uses the following Python libraries:

- `os`
- `shutil`
- `subprocess`
- `sys`

## License

This project is licensed under the MIT License.
