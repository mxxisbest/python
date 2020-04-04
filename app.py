import redis

r2 = redis.Redis(host="redis-18384.c1.ap-southeast-1-1.ec2.cloud.redislabs.com", port="18384", db=0, password="DwexJEGVBnhUSA8vyLUiTzATOb8eFNTy")
r = redis.Redis(host="redis", port="6379", db=0, password="")

for k in r.keys("*"):
    v = r.get(k)
    r2.set(k, v)
