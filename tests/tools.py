"""Module for storing testing tools (base class implementations and factories)."""
from typing import Generic, ParamSpec, TypeVar, cast

import factory

from yaeb.base.events import BaseEvent
from yaeb.bus import DictEventHandlerRegistry, EventBus

T = TypeVar('T')
P = ParamSpec('P')


class BaseFactory(Generic[T], factory.Factory):
    """Base factory boy factory with proper typing."""

    @classmethod
    def create(cls, *args: P.args, **kwargs: P.kwargs) -> T:
        """Create an object."""
        return cast(T, super().create(**kwargs))


class DictEventHandlerRegistryFactory(BaseFactory[DictEventHandlerRegistry]):
    """Dict event handler registry factory."""

    class Meta:
        """Dict event handler registry factory config."""

        model = DictEventHandlerRegistry


class EventBusFactory(BaseFactory[EventBus]):
    """Event bus factory."""

    class Meta:
        """Event bus factory config."""

        model = EventBus

    event_handler_registry = factory.SubFactory(DictEventHandlerRegistryFactory)


class Event(BaseEvent):
    """Testing event."""
