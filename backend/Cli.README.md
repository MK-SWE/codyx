### CodyX Admin Console :computer:

CodyX is a command-line interface (CLI) designed for the administration of the Guidy platform. It provides a set of commands for managing users, admins, and challenges within the system.

#### Key Features :key:

- **Interactive Command Loop:** Handles commands in an interactive shell environment.
- **Signal Handling:** Gracefully handles `KeyboardInterrupt` signals to quit the application.
- **Dynamic Command Processing:** Supports pre-processing and post-processing of commands.
- **Instance Management:** Allows creation, listing, showing, updating, and deleting instances of various types (User, Admin, Challenge).
- **Argument Parsing:** Parses command-line arguments into a dictionary for easy handling.
- **Count Instances:** Counts the number of instances for each type.
- **Customizable Prompt:** Displays a customizable command prompt.
- **Support for Non-Interactive Mode:** Adjusts behavior when running in a non-interactive environment.

#### Commands

- `all [Object Type]`: Lists all instances of a given type or all types if no type is specified.
- `create <Object Type> <Attribute1=Value1> <Attribute2=Value2> ...`: Creates a new instance of the specified object type with given attributes.
- `show <Object Type> <Instance ID>`: Displays the details of a specific instance.
- `destroy <Object Type> <Instance ID>`: Deletes a specific instance.
- `update <Object Type> <Instance ID> <Key> <Value>`: Updates the specified attribute of an instance.
- `count [Object Type]`: Counts the number of instances of a given type or all types if no type is specified.
- `quit`: Exits the console.

## Usage

To start the CodyX console, run the `cli.py` script from your terminal. Once the console is running, you can enter any of the supported commands.

Example:

```bash
$ python Cli.py
CodyX> create User email='test@mail.com' username='TestUser' password='Test.1234' full_name='Test User'
Instance Created with The id: 4c093875-3054-4b25-9520-80ba3edb02a2
email: test@mail.com
username: TestUser
password: Test.1234
full_name: Test User
CodyX> show User 4c093875-3054-4b25-9520-80ba3edb02a2

[User] (4c093875-3054-4b25-9520-80ba3edb02a2)
{'badges': '[]', 'username': 'TestUser', 'starred_challenges': '[]', 'active': True, 'role': 'user', 'created_at': '17-07-2024 21:59:34', 'email': 'test@mail.com', 'full_name': 'Test User', 'points': 0, 'authenticated': False, 'id': '4c093875-3054-4b25-9520-80ba3edb02a2', 'updated_at': '17-07-2024 21:59:34'}

CodyX> quit

Quitting...
```
