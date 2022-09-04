"""Module storing base event handler registry class."""
from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Any, Type

if TYPE_CHECKING:
    from yaeb.base.events import AllEvents, BaseEvent
    from yaeb.base.handlers import BaseEventHandler


class BaseEventHandlerRegistry(abc.ABC):
    """Registry handling adding/getting event handlers using any storage."""

    @abc.abstractmethod
    def add_event_handler(
        self,
        event_type: Type[BaseEvent] | Type[AllEvents],
        event_handler: BaseEventHandler[Any],
    ) -> None:
        """Add event handler for given event type to registry."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_event_handlers(
        self,
        event_type: Type[BaseEvent] | Type[AllEvents],
    ) -> tuple[BaseEventHandler[Any], ...]:
        """Get event handlers for given event type from registry."""
        raise NotImplementedError
