import abc

import pydantic


class Class:
    def bad_method(this):
        pass

    if False:

        def extra_bad_method(this):
            pass

    def good_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @abc.abstractclassmethod
    def abstract_class_method(cls):
        pass

    @staticmethod
    def static_method(x):
        return x

    @pydantic.validator
    def lower(cls, my_field: str) -> str:
        pass

    @pydantic.validator("my_field")
    def lower(cls, my_field: str) -> str:
        pass

    def __init__(self):
        ...

    def __new__(cls, *args, **kwargs):
        ...

    def __init_subclass__(self, default_name, **kwargs):
        ...


class MetaClass(abc.ABCMeta):
    def bad_method(self):
        pass

    def good_method(cls):
        pass


def func(x):
    return x


class PosOnlyClass:
    def good_method_pos_only(self, blah, /, something: str):
        pass

    def bad_method_pos_only(this, blah, /, self, something: str):
        pass
