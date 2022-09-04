"""Module containing event bus implementation & handler description."""
import dataclasses
from typing import Any, Type

from yaeb.base.bus import BaseEventBus
from yaeb.base.events import AllEvents, BaseEvent
from yaeb.base.handlers import BaseEventHandler
from yaeb.base.registry import BaseEventHandlerRegistry


@dataclasses.dataclass
class DictEventHandlerRegistry(BaseEventHandlerRegistry):
    """Registry storing event handlers in memory."""

    event_handlers: dict[
        Type[BaseEvent] | Type[AllEvents],
        list[BaseEventHandler[Any]],
    ] = dataclasses.field(default_factory=dict)

    def add_event_handler(
        self,
        event_type: Type[BaseEvent] | Type[AllEvents],
        event_handler: BaseEventHandler[Any],
    ) -> None:
        """Add event handler for given event type to in memory storage."""
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []

        self.event_handlers[event_type].append(event_handler)

    def get_event_handlers(
        self,
        event_type: Type[BaseEvent] | Type[AllEvents],
    ) -> tuple[BaseEventHandler[Any], ...]:
        """Get stored in memory event handlers for given event type."""
        return tuple(self.event_handlers.get(event_type, []))


@dataclasses.dataclass
class EventBus(BaseEventBus):
    """Implementation of the event bus."""

    event_handler_registry: BaseEventHandlerRegistry

    def register(
        self,
        event_type: Type[BaseEvent] | Type[AllEvents],
        event_handler: BaseEventHandler[Any],
    ) -> None:
        """Register handler for given event."""
        self.event_handler_registry.add_event_handler(event_type, event_handler)

    def emit(self, event: BaseEvent) -> None:
        """Send event to bus executing all registered handlers."""
        all_events_handlers = self.event_handler_registry.get_event_handlers(AllEvents)

        for all_events_handler in all_events_handlers:
            all_events_handler.execute(event=event, bus=self)

        event_handlers = self.event_handler_registry.get_event_handlers(type(event))

        for event_handler in event_handlers:
            event_handler.execute(event=event, bus=self)
