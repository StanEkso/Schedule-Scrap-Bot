from shared.services.config import configService
from shared.logger.logger import logger
WRITE_LOGS = not not configService.get("WRITE_LOGS") or False


def InvokeLog(func):
    if not WRITE_LOGS:
        return func

    def wrapper(*args, **kwargs):
        logger.custom(
            f"Function {func.__name__} executed with args: {args} and kwargs: {kwargs}.", "INVOKE")
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper


def InvokePerformance(func):
    if not WRITE_LOGS:
        return func

    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        logger.custom("Function {} executed in {:.2f} seconds.".format(
            func.__name__, end - start), "PERFORMANCE")
        return result
    wrapper.__name__ = func.__name__
    return wrapper


def InvokePerformanceAsync(func):
    if not WRITE_LOGS:
        return func

    async def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = await func(*args, **kwargs)
        end = time.time()

        logger.custom("Function {} executed in {:.2f} seconds.".format(
            func.__name__, end - start), "PERFORMANCE")
        return result
    wrapper.__name__ = func.__name__
    return wrapper
