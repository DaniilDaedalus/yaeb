"""Module containing event bus interfaces."""
from __future__ import annotations

import abc
from typing import Any, Generic, Type, TypeVar, final


class Event(abc.ABC):
    """Base class for events."""


@final
class AllEvents:
    """Event type allowing to subscribe to all events."""


E = TypeVar('E', bound=Event)


class EventHandler(abc.ABC, Generic[E]):
    """Base class for event handlers."""

    @abc.abstractmethod
    def handle_event(self, event: E, bus: EventBusInterface) -> None:
        """Handle given event."""
        raise NotImplementedError


class AsyncEventHandler(abc.ABC, Generic[E]):
    """Base class for async event handlers."""

    async def handle_event(self, event: E, bus: EventBusInterface) -> None:
        """Handle given event asynchronously."""
        raise NotImplementedError


class EventHandlerRegistry(abc.ABC):
    """Registry handling adding/getting event handlers using any storage."""

    @abc.abstractmethod
    def add_event_handler(
        self,
        event_type: Type[Event] | Type[AllEvents],
        event_handler: EventHandler[Any] | AsyncEventHandler[Any],
    ) -> None:
        """Add event handler for given event type to registry."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_event_handlers(
        self,
        event_type: Type[Event] | Type[AllEvents],
    ) -> tuple[EventHandler[Any] | AsyncEventHandler[Any], ...]:
        """Get event handlers for given event type from registry."""
        raise NotImplementedError


class EventBusInterface(abc.ABC):
    """Base event bus interface."""

    @abc.abstractmethod
    def register(
        self,
        event_type: Type[Event] | Type[AllEvents],
        event_handler: EventHandler[Any] | AsyncEventHandler[Any],
    ) -> None:
        """Register handler for given event."""
        raise NotImplementedError

    @abc.abstractmethod
    def emit(self, event: Event) -> None:
        """Send event to bus executing all registered handlers."""
        raise NotImplementedError
