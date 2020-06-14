# import redis
# pool=redis.ConnectionPool(host='localhost',port=6379,db=0)
# r = redis.StrictRedis(connection_pool=pool)
# r.set('foo', 'Bar')
# r.expire('foo', 60)
from app.libs.redis_lock import redis_lock
from app.libs.redis_client import RedisClient


@redis_lock(RedisClient.get_client(), "send_mail", wait_time=60, wait_msg="60秒内只能发送一次邮件")
def send_mail():
    print("sdfasd")


if __name__ == '__main__':
    for i in range(10):
        send_mail()
