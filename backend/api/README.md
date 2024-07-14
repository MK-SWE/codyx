## CodyX Web Application

CodyX is a Flask-based web application designed to provide a comprehensive platform for users to interact with various features. This document outlines the structure of the application and its components, including blueprints for modular development and configuration settings for environment management.

### Application Structure

The CodyX application is structured around Flask blueprints, allowing for a modular and scalable approach to building web applications. Each blueprint represents a distinct component of the application, such as user authentication, landing pages, and other functionalities.

### Blueprints

- [**`Views`**](./blueprints/views.py): Handles the routing and logic for the application's static pages, including the landing, about, contact, terms, and privacy pages.
- **Auth** (Not included in the current context): Manages user authentication, registration, and session management.

### Configuration

The application's configuration is managed through the [`Config`](./blueprints/config.py) class, which reads environment variables to set up various aspects of the application, such as database connections, session management, and security settings.

### Running the Application

Before running the CodyX application, you need to set up the `.api.env` file which contains essential environment variables for the application's configuration.
This file should be located in the `/backend/api` directory of the project.

#### Steps to Create the `.api.env` File

1. Open a text editor of your choice.
2. Add the following content to the file:

    ```properties
    SECRET_KEY = "your_secret_key_here"
    SECURITY_PASSWORD_SALT = "your_security_password_salt_here"
    REDIS_URL = "redis://host:port/db"
    ```

    Replace `your_secret_key_here` and `your_security_password_salt_here` with strong, unique values. The `REDIS_URL` is set to connect to a local Redis server by default; modify this if your Redis setup differs.

3. Save the file as `/backend/api/.api.env`.

#### Important Notes

- **Do not commit this file to version control**. It contains sensitive information that should not be shared publicly. Ensure `.api.env` is listed in your `.gitignore` file.
- The application reads from this file to configure various aspects, such as security settings and connections to external services like Redis. It's crucial for the proper operation of your CodyX application.

By following these steps, you will have created the necessary environment file for the CodyX application, allowing it to run with your specific configurations.

To run the CodyX application, a script named [`run.sh`](./run.sh) is provided.
This script simplifies the process of starting the Flask development server with the necessary environment variables and configurations.

#### Usage

To start the application using the `run.sh` script, follow these steps:

1. Ensure that the script has execute permissions:
    ```bash
    $ chmod +x run.sh
    ```
2. Run the application:
    - in development mode:
        ```bash
        $ ./run.sh dev 0.0.0.0 5000
        Starting the app server on host: 0.0.0.0 and port: 5000
        * Serving Flask app './api/app.py'
        * Debug mode: off
        WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
        * Running on all addresses (0.0.0.0)
        * Running on http://127.0.0.1:5000
        * Running on http://***.**.*.***:5000
        Press CTRL+C to quit
        ```
    - in debug mode:
        ```bash
        $ ./run.sh debug 0.0.0.0 5000
        Starting the app server on host: 0.0.0.0 and port: 5000
        * Serving Flask app './api/app.py'
        * Debug mode: on
        WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
        * Running on all addresses (0.0.0.0)
        * Running on http://127.0.0.1:5000
        * Running on http://***.**.*.***:5000
        Press CTRL+C to quit
        * Restarting with stat
        * Debugger is active!
        * Debugger PIN: 123-456-789
        ```
3. Access the application in a web browser by navigating to the provided URL (e.g., `http://0.0.0.0:5000`).
