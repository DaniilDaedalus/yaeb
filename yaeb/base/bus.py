"""Module storing base event bus."""
from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Any, Type

if TYPE_CHECKING:
    from yaeb.base.events import AllEvents, BaseEvent
    from yaeb.base.handlers import BaseEventHandler


class BaseEventBus(abc.ABC):
    """Base event bus interface."""

    @abc.abstractmethod
    def register(
        self,
        event_type: Type[BaseEvent] | Type[AllEvents],
        event_handler: BaseEventHandler[Any],
    ) -> None:
        """Register handler for given event."""
        raise NotImplementedError

    @abc.abstractmethod
    def emit(self, event: BaseEvent) -> None:
        """Send event to bus executing all registered handlers."""
        raise NotImplementedError
