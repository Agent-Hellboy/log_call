import functools
import inspect
import logging
from typing import Callable, Dict, List, Any

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)


def prepare_response(func: str, args_dict: Dict) -> str:
    return f"{func} called with {args_dict}"


def get_log_stmt(func: Callable, args_v: List, kwargs_v: Dict) -> str:
    args_dict: Dict = {}
    all_args_val = inspect.getfullargspec(func)
    args = all_args_val.args
    args_v = list(args_v)
    if args:
        for i in range(len(args)):
            if args[i] != 'self':
                args_dict[args[i]] = args_v[i]
                args_v.pop(0)
    args_dict['args'] = args_v
    args_dict['kwargs'] = kwargs_v
    return prepare_response(func.__name__, args_dict)


def logger(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        log_stmt = get_log_stmt(func, args, kwargs)
        logging.info(f"{log_stmt}")
        return func(*args, **kwargs)
    return wrapper


def log_call(obj: Callable[..., Any]) -> Callable:
    if inspect.isfunction(obj):
        return logger(obj)
        
    if inspect.isclass(obj):
        class Wrapper(obj):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def __getattribute__(self, attr):
                attr = object.__getattribute__(self, attr)
                return logger(attr) if callable(attr) else attr

        return Wrapper