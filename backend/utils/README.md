### `DBStorage` :floppy_disk:

The `DBStorage` class is a comprehensive `MySQL` database storage system designed for efficient data management within the CodyX project. It utilizes the Singleton pattern to ensure that only one instance of the database connection is created throughout the application's lifecycle.

#### Configuration :gear:
The database connection is configured through environment variables defined in the `.utils.env` file located within the `utils` directory. The following variables are required:
> Please ensure that the `.utils.env` file is correctly configured with your database credentials and environment settings.
> Don't use this class directly in your code, use the `STORAGE` variable from [Init File](./__init__.py) instead.

- `DBUSER`: The username for the database (e.g., `"root"`).
- `DBPWD`: The password for the database user (e.g., `"pass"`).
- `HOST`: The hostname where the database server is running (e.g., `"localhost"`).
- `DB`: The name of the database to connect to (`"codyx_dev"` || `"codyx_test"`).
- `ENV`: The environment the application is running in ( `"dev"` || `"test"`).

#### Key Features :key:

- **Singleton Pattern**: Ensures a single database connection, reducing overhead.
- **Session Management**: Provides methods to manage database sessions, including creation, querying, and transaction management.
- **CRUD Operations**: Supports Create, Read, Update, and Delete operations through intuitive methods.
- **Environment-Specific Configuration**: Allows for different configurations based on the application environment, facilitating easy transitions between development, testing, and production.

#### Methods :wrench:

- `session()`: Returns the current database session.
- `all(cls=None)`: Queries all objects of a given class from the database. If no class is specified, queries all objects.
- `new(obj)`: Adds a new object to the current database session.
- `save()`: Commits all changes made during the current database session.
- `delete(obj=None)`: Deletes a specified object from the current database session.
- `reload()`: Initializes the database connection and session.
- `close()`: Closes the current database session.
- `get(cls, id)`: Retrieves a single object by its class and ID.
- `count(cls=None)`: Counts the number of objects in storage, optionally filtered by class.
- `query(cls)`: Initiates a query on the current database session for a specific class.
- `rollback()`: Rolls back the current transaction in the session.

#### Environment Setup :world_map:

To set up the environment for `DBStorage`, ensure that the `.utils.env` file is correctly configured with your database credentials and environment. The class automatically loads these settings upon instantiation.

For more information on using `DBStorage` within your project, refer to the class documentation and method docstrings.
