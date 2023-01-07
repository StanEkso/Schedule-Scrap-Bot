from shared.services.config import configService
WRITE_LOGS = not not configService.get("WRITE_LOGS") or False


def InvokeLog(func):
    if not WRITE_LOGS:
        return func

    def wrapper(*args, **kwargs):
        print(
            f"[INVOKE] Function {func.__name__} executed with args: {args} and kwargs: {kwargs}.")
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
        print(
            "[PERFORMANCE] Function {} executed in {:.2f} seconds.".format(
                func.__name__, end - start))
        return result
    wrapper.__name__ = func.__name__
    return wrapper
