## Project Models :file_folder:

### [`BaseModel`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2FCodyX%2Fbackend%2Fmodels%2Fbase.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A12%2C%22character%22%3A6%7D%5D "backend/models/base.py") :floppy_disk:

The [`BaseModel`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2FCodyX%2Fbackend%2Fmodels%2Fbase.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A12%2C%22character%22%3A6%7D%5D "backend/models/base.py") class serves as the foundation for all models within the CodyX project, providing a unified structure and common attributes for data representation. It is designed to be extended by other model classes, ensuring consistency and efficiency in data handling.

#### Attributes :bookmark_tabs:
The [`BaseModel`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2FCodyX%2Fbackend%2Fmodels%2Fbase.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A12%2C%22character%22%3A6%7D%5D "backend/models/base.py") defines essential attributes that are common across all models in the application:
- `id` (str): A unique identifier for each model instance.
- `created_at` (datetime): The date and time when the model instance was created.
- [`updated_at`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2FCodyX%2Fbackend%2Fmodels%2Fuser.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A47%2C%22character%22%3A13%7D%5D "backend/models/user.py") (datetime): The date and time when the model instance was last updated.

#### Key Features :key:
- **Abstraction**: Serves as an abstract base class that other models inherit from, providing a common set of attributes and methods.
- **Automatic ID Generation**: Automatically generates a unique `id` for each instance if not provided.
- **Timestamp Management**: Automatically handles the creation and update timestamps for each instance.
- **Dictionary Representation**: Allows model instances to be easily converted to dictionaries for serialization and storage.
- **String Representation**: Provides a human-readable string representation of model instances.

#### Methods :wrench:
- [`__init__(*args, **kwargs)`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2FCodyX%2Fbackend%2Fmodels%2Fchallenge.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A20%2C%22character%22%3A8%7D%5D "backend/models/challenge.py"): Initializes a new instance of a model, setting attributes from keyword arguments.
- [`save()`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2FCodyX%2Fbackend%2Fmodels%2Fbase.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A52%2C%22character%22%3A8%7D%5D "backend/models/base.py"): Saves the model instance to the database, updating the [`updated_at`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2FCodyX%2Fbackend%2Fmodels%2Fuser.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A47%2C%22character%22%3A13%7D%5D "backend/models/user.py") timestamp.
- [`delete()`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2FCodyX%2Fbackend%2Fmodels%2Fbase.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A59%2C%22character%22%3A8%7D%5D "backend/models/base.py"): Deletes the model instance from the database.
- `to_dict()`: Returns a dictionary representation of the model instance, excluding sensitive or unnecessary fields.
- `__str__()`: Returns a string representation of the model instance, including the class name, `id`, and dictionary representation.

#### Usage :computer:
To use [`BaseModel`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2FCodyX%2Fbackend%2Fmodels%2Fbase.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A12%2C%22character%22%3A6%7D%5D "backend/models/base.py"), create a new model class that inherits from it and define any additional attributes or methods specific to that model.

#### Example: User Model
```python
class User(BaseModel):
    """User model, inheriting from BaseModel"""
    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    ...
```

### `User` :bust_in_silhouette:

The `User` class represents users of the CodyX platform, extending the `BaseModel` with user-specific attributes and methods.

#### Attributes :bookmark_tabs:
- `email` (String): The user's email address, unique across the platform.
- `username` (String): The user's chosen username, unique across the platform.
- `_password` (String): The user's hashed password (not directly accessible).
- `first_name` (String): The user's first name.
- `last_name` (String): The user's last name.
- `active` (Boolean): Whether the user's account is active.
- `authenticated` (Boolean): Whether the user is currently authenticated.
- `role` (String): The user's role within the platform (e.g., 'user', 'admin').

#### Key Features :key:
- **Password Hashing**: Securely hashes and stores user passwords.
- **Authentication and Authorization**: Supports checking user credentials and roles.
- **Profile Management**: Allows users to edit their profile and password.

### `Admin` :crown:

The `Admin` class represents administrative users, inheriting from the `User` class and adding administrative-specific methods.

#### Key Features :key:
- **Challenge Management**: Allows admins to add, edit, and remove challenges.
- **Account Suspension**: Enables admins to suspend user accounts.

### `Challenge` :trophy:

The `Challenge` class represents coding challenges on the CodyX platform, extending the `BaseModel` with challenge-specific attributes.

#### Attributes :bookmark_tabs:
- `name` (String): The name of the challenge.
- `description` (String): A detailed description of the challenge.
- `ex_input` (String): Example input for the challenge.
- `output` (String): Expected output for the given example input.
- `difficulty` (String): The difficulty level of the challenge.
- `_starter_function` (JSON): A JSON object representing the starter code for the challenge.
- `examples` (String): Example cases for the challenge.
- `stars` (Integer): The number of stars the challenge has received.
- `solved` (Integer): The number of times the challenge has been solved.

#### Key Features :key:
- **Starter Function Management**: Allows for the storage and retrieval of starter functions without additional backslashes.
- **Difficulty Levels**: Challenges can be categorized by difficulty.
- **Engagement Metrics**: Tracks stars and solved counts to gauge user engagement.