"""Module containing event bus interfaces."""
from __future__ import annotations

import abc
import asyncio
from collections import deque
from typing import Any, Generic, Type, TypeVar, final


class BaseEvent(abc.ABC):
    """Base class for events."""

    parent_event: BaseEvent | None

    def __init__(self, parent_event: BaseEvent | None) -> None:
        """Add parent event for further tracking."""
        self.parent_event = parent_event

    def get_history(self) -> tuple[BaseEvent, ...]:
        """Get history of events resulted current event to be emitted."""
        history: deque[BaseEvent] = deque()

        parent_event = self.parent_event
        while parent_event is not None:
            history.appendleft(parent_event)
            parent_event = parent_event.parent_event

        return tuple(history)


@final
class AllEvents:
    """Event type allowing to subscribe to all events."""


E = TypeVar('E', bound=BaseEvent)


class BaseEventHandler(abc.ABC, Generic[E]):
    """Base class for event handlers."""

    @abc.abstractmethod
    def execute(self, event: E, bus: BaseEventBus) -> None:
        """Execute handling of event."""
        raise NotImplementedError


class BaseAsyncEventHandler(BaseEventHandler[E]):
    """Base class for async event handlers."""

    @abc.abstractmethod
    async def handle_event(self, event: E, bus: BaseEventBus) -> None:
        """Handle given event asynchronously."""
        raise NotImplementedError

    def execute(self, event: E, bus: BaseEventBus) -> None:
        """Execute event handling via asyncio task asynchronously."""
        asyncio.Task(self.handle_event(event=event, bus=bus))


class BaseSyncEventHandler(BaseEventHandler[E]):
    """Base class for sync event handlers."""

    def handle_event(self, event: E, bus: BaseEventBus) -> None:
        """Handle given event synchronously."""
        raise NotImplementedError

    def execute(self, event: E, bus: BaseEventBus) -> None:
        """Execute handling of event simply by calling handle event method."""
        self.handle_event(event=event, bus=bus)


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
