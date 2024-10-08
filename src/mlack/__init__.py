import inspect

import httpretty
import functools

from slack_sdk import WebClient

from .injector import inject


# Create the wrapper class
def dev_mode_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inject()
        try:
            return func(*args, **kwargs)
        finally:
            httpretty.disable()
            httpretty.reset()

    return wrapper


class MockClient(WebClient):
    def __init__(self, token: str, *args, **kwargs):
        super().__init__(token, *args, **kwargs)
        self._apply_decorators()

    def _apply_decorators(self):
        webclient_methods = {
            name
            for name, _ in inspect.getmembers(WebClient, predicate=inspect.isfunction)
        }
        for method_name in dir(self):
            if not method_name.startswith("_") and method_name in webclient_methods:
                method = getattr(self, method_name)
                if callable(method):
                    decorated_method = dev_mode_decorator(method)
                    setattr(self, method_name, decorated_method)
                    print(f"Decorated {method_name}")
                    if method_name == "users_conversations":
                        print("The func is", method)

    def __getattr__(self, name):
        # Delegate attribute access to the wrapped client
        return getattr(self, name)
