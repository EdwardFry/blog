from functools import wraps

def decorator(func):
    @wraps(func)
    def _inner(*args, **kwargs):
        # do something before function runs.
        func(*args, **kwargs)
        # do something after function has run.
    return _inner

