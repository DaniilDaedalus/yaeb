"""Module containing base type annotated factiry."""
from typing import Generic, ParamSpec, TypeVar, cast

import factory

T = TypeVar("T")
P = ParamSpec("P")


class BaseFactory(Generic[T], factory.Factory):
    """Base factory boy factory with proper typing."""

    @classmethod
    def create(cls, *args: P.args, **kwargs: P.kwargs) -> T:
        """Create an object."""
        return cast(T, super().create(**kwargs))
