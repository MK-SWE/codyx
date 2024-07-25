from redis import Redis
from uuid import uuid4


class Cache:
    """
    A class that provides caching functionality using Redis.

    Attributes:
      _redis (Redis): An instance of the Redis client.
    """

    def __init__(self, host, port, db):
        """
        Initializes a new instance of the Cache class.

        It creates a Redis client and flushes the Redis database.
        """
        self.HOST = host
        self.PORT = port
        self.DB = db

        self._redis = Redis(host=self.HOST, port=self.PORT, db=self.DB)
        self._redis.flushdb()

    def store(self, data, key=str(uuid4())) -> str:
      """
      Stores the provided data in the cache.

      Args:
        key (str, optional): The key associated with the data. Defaults to a new UUID.
        data: The data to be stored in the cache.

      Returns:
        str: The key associated with the stored data.
      """
      self._redis.set(key, data)
      return key

    def get(self, key: str) -> str:
        """
        Retrieves the data associated with the provided key from the cache.

        Args:
          key (str): The key associated with the data.

        Returns:
          str: The data associated with the provided key.
        """
        value = self._redis.get(key)
        if value is not None:
            return value.decode('utf-8')  # Decode the bytes object to a string
        return None

    def delete(self, key: str) -> None:
        """
        Deletes the data associated with the provided key from the cache.

        Args:
          key (str): The key associated with the data.
        """
        self._redis.delete(key)
        return

    def update(self, key: str, data) -> None:
        """
        Updates the data associated with the provided key in the cache.

        Args:
          key (str): The key associated with the data.
          data: The new data to be associated with the key.
        """
        self._redis.set(key, data)
        return
