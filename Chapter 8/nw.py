# 8.11
import redis
conn = redis.Redis('localhost', 6379)

conn.hset('test', {'count': 1, 'name': 'Fester Bestertester'})

conn.hgetall('test')
