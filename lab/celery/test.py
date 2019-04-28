import redis
from tasks import add

# Call task
res = add.delay(4, 4)
# Check task status
res.ready() #True
# Get key
print(res)
# Get result
print(res.get())

# Check redis
rs = redis.Redis(host="127.0.0.1", port=6379, db=0)
print(rs.keys())
rs.flushall()