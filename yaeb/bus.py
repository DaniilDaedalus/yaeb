"""Module containing event bus implementation & handler description."""
from __future__ import annotations

import abc
from typing import Any, Generic, Type, TypeVar, final


class Event(abc.ABC):
    """Base class for events."""


@final
class AllEvents:
    """Event type allowing to subscribe to all events."""


GenericEvent = TypeVar('GenericEvent', bound=Event)


class EventHandler(abc.ABC, Generic[GenericEvent]):
    """Base class for event handlers."""

    @abc.abstractmethod
    def handle_event(self, event: GenericEvent, bus: EventBus) -> None:
        """Handle any given event."""
        raise NotImplementedError


class EventBus:
    """Implementation of the event bus."""

    event_handlers: dict[Type[Event] | Type[AllEvents], list[EventHandler[Any]]] = {}

    def register(
        self,
        event_type: Type[Event] | Type[AllEvents],
        event_handler: EventHandler[Any],
    ) -> None:
        """Register handler for given event."""
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []

        self.event_handlers[event_type].append(event_handler)

    def emit(self, event: Event) -> None:
        """Send event to bus executing all registered handlers."""
        for all_events_handler in self.event_handlers.get(AllEvents, []):
            all_events_handler.handle_event(event, self)

        for event_handler in self.event_handlers.get(type(event), []):
            event_handler.handle_event(event, self)
