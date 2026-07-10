import json
import os

from dotenv import load_dotenv

from app.cache.redis_client import redis_client

load_dotenv()

DEFAULT_TTL = int(
    os.getenv("REDIS_DEFAULT_TTL", "300")
)


class CacheService:

    def get(self, key: str):

        value = redis_client.get(key)

        if value:
            return json.loads(value)

        return None

    def set(self, key: str, value, ttl: int = DEFAULT_TTL):

        redis_client.setex(
            key,
            ttl,
            json.dumps(value)
        )

    def delete(self, key: str):

        redis_client.delete(key)

    def exists(self, key: str):

        return redis_client.exists(key)

    def ttl(self, key: str):

        return redis_client.ttl(key)

    def clear(self):

        redis_client.flushdb()