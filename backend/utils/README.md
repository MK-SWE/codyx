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

### `Cache` :zap:

The `Cache` class provides a robust Redis-based caching system designed to enhance data retrieval efficiency in the CodyX project. It leverages Redis, a high-performance in-memory data store, to cache data, reducing the need to repeatedly access slower, disk-based databases.

#### Configuration :gear:
The cache system is configured through direct parameters passed to the `Cache` class constructor. These parameters include the host, port, and database index for the Redis server. Ensure that your Redis server is running and accessible through these configurations.

- `HOST`: The hostname where the Redis server is running (e.g., `"localhost"`).
- `PORT`: The port on which the Redis server is listening (e.g., `6379`).
- `DB`: The database index to use within the Redis server (e.g., `0`).

#### Key Features :key:

- **Simplicity and Efficiency**: Provides a straightforward interface for caching data, making retrieval operations faster and more efficient.
- **Flexible Data Handling**: Supports storing, retrieving, updating, and deleting operations for cached data.
- **Automatic Key Generation**: Generates a unique UUID for each cached item if no key is provided, simplifying data storage.
- **Direct Redis Integration**: Utilizes the Redis client directly, offering high performance and reliability.

#### Methods :wrench:

- `store(data, key=str(uuid4())) -> str`: Stores the provided data in the cache, automatically generating a key if not provided.
- `get(key: str) -> str`: Retrieves the data associated with the provided key from the cache.
- `delete(key: str) -> None`: Deletes the data associated with the provided key from the cache.
- `update(key: str, data) -> None`: Updates the data associated with the provided key in the cache.

#### Environment Setup :world_map:

To set up the environment for `Cache`, ensure that your Redis server is correctly configured and running. The class requires direct access to the Redis server through the provided host, port, and database index parameters.

For more information on using `Cache` within your project, refer to the class documentation and method docstrings. This class is designed to be easily integrated into any project requiring caching capabilities to enhance performance and efficiency.

#### Best Practices :bulb:

- **Key Management**: Manage your keys wisely to prevent collisions. Use descriptive keys that reflect the data being stored.
- **Connection Handling**: Ensure that the Redis server is always available and that the connection parameters are correctly configured.
- **Data Serialization**: Consider serializing complex data structures before storing them in the cache to ensure compatibility and efficiency.

By following these guidelines and utilizing the `Cache` class, you can significantly improve the performance of your application by reducing data retrieval times and offloading demand from your primary data stores.