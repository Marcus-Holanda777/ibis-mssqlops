from ibis_mssqlops.consts import (
    DatePartType,
    MssqlTypeName,
    Style
)
from functools import wraps


def get_value_enums(func):
    @wraps(func)
    def inner(*args, **kwargs):
        tps = (
            Style,
            DatePartType,
            MssqlTypeName
        )

        is_enum = lambda x: isinstance(x, tps)

        args_alter = tuple(
            arg.value if is_enum(arg) 
            else arg 
            for arg in args
        )

        kwargs_alter = {
            k:v.value if is_enum(v) 
            else v 
            for k, v in kwargs.items()
        }

        return func(*args_alter, **kwargs_alter)
    return inner