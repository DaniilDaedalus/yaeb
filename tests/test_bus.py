"""Module testing event bus functionality."""
from dataclasses import dataclass

from yaeb.bus import AllEvents, Event, EventBus, EventHandler


class FakeEvent(Event):
    """Testing event."""


@dataclass
class FakeHandler(EventHandler[FakeEvent]):
    """Testing handler recording calls to it's handle_event."""

    is_called: bool

    def handle_event(self, event: FakeEvent, bus: EventBus) -> None:
        """Record call to this handler ignoring event."""
        self.is_called = True


def test_bus() -> None:
    """Test that event bus is capable of registering & emitting events."""
    # Given: Empty bus & test event handler
    bus = EventBus()

    fake_handler = FakeHandler(is_called=False)

    # When: Test event handler is registered for event & corresponding event is emitted
    bus.register(FakeEvent, fake_handler)
    bus.emit(FakeEvent())

    # Then: Test event handler is called
    assert fake_handler.is_called


def test_all_events_registration() -> None:
    """Test that event bus is capable of registering for all events."""
    # Given: Empty bus & test event handler
    bus = EventBus()

    fake_handler = FakeHandler(is_called=False)

    # When: Test event handler is registered for all events & any event is emitted
    bus.register(AllEvents, fake_handler)
    bus.emit(Event())

    # Then: Test event handler is called
    assert fake_handler.is_called
