import redis

# Connect to Redis server in WSL
redis_host = 'localhost'
redis_port = 6379
redis_db = 0

R = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)


