## Project Setup Files :hammer_and_wrench:

This document provides an overview of the setup scripts and SQL files used to configure the development and testing environments for the project.

### Redis Installation Script

The [`install redis`](./db/install-redis.sh) script automates the process of downloading, extracting, building, and installing Redis on an Ubuntu system. It also configures Redis to start on boot and listens on the default port 6379.

#### Key Steps:

1. **Download Redis**: Fetches the stable version of Redis.
2. **Extract and Build**: Extracts the Redis archive and builds it from source.
3. **Install**: Moves the Redis binaries to `/usr/local/bin` and adds them to the system PATH.
4. **Clean Up**: Removes temporary files and directories.
5. **Configure Redis**: Edits the Redis configuration to listen on all local ports and sets other default settings.
6. **Service Management**: Provides commands to start, stop, and check the status of the Redis server.

#### Usage:

To install Redis, simply run the script:

```bash
./install-redis.sh
```

### MySQL Setup Scripts
Two SQL scripts are provided to prepare the MySQL server for the project, one for the development environment and another for the testing environment.

#### [**`Development Database`**](./db/setup_mysql_dev.sql)
- Creates the `codyx_dev` database.
- Grants all privileges on this database to the `root` user.

#### [**`Testing Database`**](./db/setup_mysql_test.sql)
- Creates the codyx_test database.
- Grants all privileges on this database to the root user.

#### Usage:
To set up the MySQL databases:
- log into your MySQL server as the root user and execute the scripts
- or use the following commands:
    ```bash
    $ mysql -u root -p < setup_mysql_dev.sql
    $ mysql -u root -p < setup_mysql_test.sql
    ```
