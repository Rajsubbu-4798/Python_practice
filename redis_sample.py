
import redis
r=redis.Redis()
r.mset({"raj":"23"})
print(r.get("raj"))

