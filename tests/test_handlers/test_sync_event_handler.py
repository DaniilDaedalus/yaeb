"""Module testing sync event handler's functionality."""
from tests.factories.bus import EventBusFactory
from yaeb.base.bus import BaseEventBus
from yaeb.base.events import BaseEvent
from yaeb.base.handlers import BaseSyncEventHandler


class SyncEventHandler(BaseSyncEventHandler[BaseEvent]):
    """Sync event handler recording calls to itself."""

    is_called: bool

    def handle_event(self, event: BaseEvent, bus: BaseEventBus) -> None:
        """Record call to this handler ignoring event."""
        self.is_called = True


def test_sync_event_handler() -> None:
    """Test that sync event handler works properly."""
    # Given: sync event handler
    sync_event_handler = SyncEventHandler()

    # When: handler's execute is called
    sync_event_handler.execute(
        event=BaseEvent(parent_event=None),
        bus=EventBusFactory.create(),
    )

    # Then: handler is called synchronously
    assert sync_event_handler.is_called
