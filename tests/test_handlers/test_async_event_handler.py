"""Module testing async event handler functionality."""
import asyncio

from tests.factories.bus import EventBusFactory
from yaeb.base.bus import BaseEventBus
from yaeb.base.events import BaseEvent
from yaeb.base.handlers import BaseAsyncEventHandler


class AsyncEventHandler(BaseAsyncEventHandler[BaseEvent]):
    """Async event handler recording calls to itself."""

    is_called: bool

    async def handle_event(self, event: BaseEvent, bus: BaseEventBus) -> None:
        """Record call to handler ignoring event."""
        self.is_called = True


async def test_async_event_handler() -> None:
    """Test that async event handler works properly."""
    # Given: async event handler
    async_event_handler = AsyncEventHandler()

    # When: handler's execute method is called
    async_event_handler.execute(
        BaseEvent(parent_event=None),
        bus=EventBusFactory.create(),
    )

    await asyncio.sleep(0)

    # Then: handler is called on the next event loop's cycle
    assert async_event_handler.is_called
