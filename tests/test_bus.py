"""Module testing event bus functionality."""
from tests.factories.bus import EventBusFactory
from yaeb.base.bus import BaseEventBus
from yaeb.base.events import AllEvents, BaseEvent
from yaeb.base.handlers import BaseEventHandler


class FakeHandler(BaseEventHandler[BaseEvent]):
    """Testing handler recording calls to it's `execute`."""

    is_called: bool

    def execute(self, event: BaseEvent, bus: BaseEventBus) -> None:
        """Record call to this handler ignoring event."""
        self.is_called = True


def test_bus() -> None:
    """Test that event bus is capable of registering & emitting events."""
    # Given: Empty bus & test event handler
    bus = EventBusFactory.create()

    fake_handler = FakeHandler()

    # When: Test event handler is registered for event & corresponding event is emitted
    bus.register(BaseEvent, fake_handler)
    bus.emit(BaseEvent(parent_event=None))

    # Then: Test event handler is called
    assert fake_handler.is_called


def test_all_events_registration() -> None:
    """Test that event bus is capable of registering for all events."""
    # Given: Empty bus & test event handler
    bus = EventBusFactory.create()

    fake_handler = FakeHandler()

    # When: Test event handler is registered for all events & any event is emitted
    bus.register(AllEvents, fake_handler)
    bus.emit(BaseEvent(parent_event=None))

    # Then: Test event handler is called
    assert fake_handler.is_called
