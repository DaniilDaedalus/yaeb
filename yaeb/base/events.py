"""Module storing base event models."""
from __future__ import annotations

from collections import deque
from typing import final


class BaseEvent:
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
