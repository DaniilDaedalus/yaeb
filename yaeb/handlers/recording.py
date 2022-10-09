"""Module containing recording event bus implementation."""
from typing import Type, TypeVar

from yaeb.base.bus import BaseEventBus
from yaeb.base.events import BaseEvent
from yaeb.base.handlers import BaseSyncEventHandler

T = TypeVar("T")


class RecordingEventHandler(BaseSyncEventHandler[BaseEvent]):
    """Event handler recording calls to it's handle_event."""

    recorded_events: list[BaseEvent]

    def __init__(self) -> None:
        """Initialize recorded events with an empty list."""
        self.recorded_events = []

    def handle_event(self, event: BaseEvent, bus: BaseEventBus) -> None:
        """Record handled event."""
        self.recorded_events.append(event)

    def get_recorded_event(self, event_type: Type[T]) -> T | None:
        """Get recorded event by it's type (if any)."""
        for recorded_event in self.recorded_events:
            if isinstance(recorded_event, event_type):
                return recorded_event

        return None
