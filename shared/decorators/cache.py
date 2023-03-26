import time
from ..logger.logger import logger


def Cache(timeout=60000):
    LAST_INVOKE_INFO = {}
    cache = {}

    def decorator(func):
        def wrapper(*args, **kwargs):
            CURRENT_TIME = current_time_millis()
            key = func.__name__ + str(args) + str(kwargs)
            if key in cache and CURRENT_TIME - LAST_INVOKE_INFO.get(key, 0) < timeout:
                logger.info("Cache " + key)
                return cache[key]
            else:
                cache[key] = func(*args, **kwargs)
                LAST_INVOKE_INFO[key] = CURRENT_TIME
                return cache[key]

        wrapper.__name__ = func.__name__
        return wrapper

    return decorator


def CoroutineCache(timeout=60000):
    LAST_INVOKE_INFO = {}
    cache = {}

    def decorator(func):
        async def wrapper(*args, **kwargs):
            CURRENT_TIME = current_time_millis()
            key = func.__name__ + str(args) + str(kwargs)
            if key in cache and CURRENT_TIME - LAST_INVOKE_INFO.get(key, 0) < timeout:
                return cache[key]
            else:
                cache[key] = await func(*args, **kwargs)
                LAST_INVOKE_INFO[key] = CURRENT_TIME
                return cache[key]

        wrapper.__name__ = func.__name__
        return wrapper

    return decorator


def current_time_millis():
    return int(round(time.time() * 1000))
