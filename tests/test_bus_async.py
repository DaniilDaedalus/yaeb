"""Module containing tests ensuring that async event handlers work properly."""
import asyncio
import dataclasses

from yaeb.base import BaseAsyncEventHandler, BaseEvent, BaseEventBus
from yaeb.bus import DictEventHandlerRegistry, EventBus


@dataclasses.dataclass
class FakeAsyncEventHandler(BaseAsyncEventHandler[BaseEvent]):
    """Test async event handling recording calls to itself."""

    is_called: bool

    async def handle_event(self, event: BaseEvent, bus: BaseEventBus) -> None:
        """Record call to this handler, ignoring event."""
        self.is_called = True


async def test_bus_async() -> None:
    """Test that event bus is able to call async handlers."""
    # Given: async event handler registered for the bus
    test_event_handler = FakeAsyncEventHandler(False)

    bus = EventBus(DictEventHandlerRegistry())
    bus.register(BaseEvent, test_event_handler)

    # When: corresponding event is called
    bus.emit(BaseEvent(parent_event=None))

    # Then: async handler is called asynchronously
    await asyncio.sleep(0)
    assert test_event_handler.is_called
