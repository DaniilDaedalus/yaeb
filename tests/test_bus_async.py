"""Module containing tests ensuring that async event handlers work properly."""
import asyncio
import dataclasses

from yaeb.bus import EventBus, NonPersistentEventHandlerRegistry
from yaeb.interface import AsyncEventHandler, Event, EventBusInterface


@dataclasses.dataclass
class TestAsyncEventHandler(AsyncEventHandler[Event]):
    """Test async event handling recording calls to itself."""

    is_called: bool

    async def handle_event(self, event: Event, bus: EventBusInterface) -> None:
        """Record call to this handler, ignoring event."""
        self.is_called = True


async def test_bus_async() -> None:
    """Test that event bus is able to call async handlers."""
    # Given: async event handler registered for the bus
    test_event_handler = TestAsyncEventHandler(False)

    bus = EventBus(NonPersistentEventHandlerRegistry())
    bus.register(Event, test_event_handler)

    # When: corresponding event is called
    bus.emit(Event())

    # Then: async handler is called asynchronously
    await asyncio.sleep(0)
    assert test_event_handler.is_called
