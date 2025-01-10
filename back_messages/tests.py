import redis
from django.conf import settings
from django.test import TestCase

class RedisConnectionTest(TestCase):
    def test_redis_connection(self):
        # Extract the Redis URL from the CHANNEL_LAYERS setting
        redis_url = settings.CHANNEL_LAYERS['default']['CONFIG']['hosts'][0]
        
        # Ensure the URL starts with the 'redis://' scheme
        if not redis_url.startswith("redis://"):
            redis_url = "redis://" + redis_url
        
        # Now use the extracted URL to connect to Redis
        redis_client = redis.StrictRedis.from_url(redis_url)

        try:
            # Test connection by pinging Redis
            response = redis_client.ping()
            self.assertTrue(response, "Successfully connected to Redis!")
        except redis.ConnectionError as e:
            self.fail(f"Error connecting to Redis: {e}")


