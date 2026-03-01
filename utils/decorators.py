import functools
import logging

logger = logging.getLogger(__name__)

def step(description):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            self.logger.info(f"STEP: {description}")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator