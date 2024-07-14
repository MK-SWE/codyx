## Project Models :file_folder:

### `BaseModel` :floppy_disk:

The `BaseModel` class serves as the foundation for all models within the CodyX project, providing a unified structure and common attributes for data representation. It is designed to be extended by other model classes, ensuring consistency and efficiency in data handling.

#### Attributes :bookmark_tabs:
The `BaseModel` defines essential attributes that are common across all models in the application:
- `id` (str): A unique identifier for each model instance.
- `created_at` (datetime): The date and time when the model instance was created.
- `updated_at` (datetime): The date and time when the model instance was last updated.

#### Key Features :key:
- **Abstraction**: Serves as an abstract base class that other models inherit from, providing a common set of attributes and methods.
- **Automatic ID Generation**: Automatically generates a unique `id` for each instance if not provided.
- **Timestamp Management**: Automatically handles the creation and update timestamps for each instance.
- **Dictionary Representation**: Allows model instances to be easily converted to dictionaries for serialization and storage.
- **String Representation**: Provides a human-readable string representation of model instances.

#### Methods :wrench:
- `__init__(*args, **kwargs)`: Initializes a new instance of a model, setting attributes from keyword arguments.
- `save()`: Saves the model instance to the database, updating the `updated_at` timestamp.
- `delete()`: Deletes the model instance from the database.
- `to_dict()`: Returns a dictionary representation of the model instance, excluding sensitive or unnecessary fields.
- `__str__()`: Returns a string representation of the model instance, including the class name, `id`, and dictionary representation.

#### Usage :computer:
To use `BaseModel`, create a new model class that inherits from it and define any additional attributes or methods specific to that model. For example:

#### Example: User Model
```python
class User(BaseModel):
    """User model, inheriting from BaseModel"""
    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    ...
```
