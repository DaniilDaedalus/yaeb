"""Module testing recording event handler."""
from tests.factories.bus import EventBusFactory
from yaeb.base.events import AllEvents, BaseEvent
from yaeb.handlers.recording import RecordingEventHandler


def test_recording_event_handler_with_event() -> None:
    """Test that recording event handler records events."""
    # Given: event bus with recording event handler registered for all events
    recording_event_handler = RecordingEventHandler()
    event_bus = EventBusFactory.create()

    event_bus.register(AllEvents, recording_event_handler)

    # When: Any event is emitted
    event_bus.emit(BaseEvent(parent_event=None))

    # Then: event is recorded and available by it's type
    recorded_event = recording_event_handler.get_recorded_event(BaseEvent)
    assert recorded_event is not None
    assert isinstance(recorded_event, BaseEvent)


def test_recording_event_handler_without_event() -> None:
    """Test that recording event handler returns None if no recorded event is found."""
    # Given: recording event handler
    recording_event_handler = RecordingEventHandler()

    # When: get_recorded_event is called when no recorded events are available
    recorded_event = recording_event_handler.get_recorded_event(BaseEvent)

    # Then: get_recorded_event returns None
    assert recorded_event is None
