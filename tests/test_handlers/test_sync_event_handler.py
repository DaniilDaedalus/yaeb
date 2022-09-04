"""Module testing sync event handler's functionality."""
from tests.tools import Event, EventBusFactory
from yaeb.base.bus import BaseEventBus
from yaeb.base.handlers import BaseSyncEventHandler


class SyncEventHandler(BaseSyncEventHandler[Event]):
    """Sync event handler recording calls to itself."""

    is_called: bool

    def handle_event(self, event: Event, bus: BaseEventBus) -> None:
        """Record call to this handler ignoring event."""
        self.is_called = True


def test_sync_event_handler() -> None:
    """Test that sync event handler works properly."""
    # Given: sync event handler
    sync_event_handler = SyncEventHandler()

    # When: handler's execute is called
    sync_event_handler.execute(
        event=Event(parent_event=None),
        bus=EventBusFactory.create(),
    )

    # Then: handler is called synchronously
    assert sync_event_handler.is_called
