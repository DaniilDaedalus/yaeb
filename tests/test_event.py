"""Test base event functionality."""
from yaeb.base import BaseEvent


class FakeFirstEvent(BaseEvent):
    """Fake first emitted event."""


class FakeSecondEvent(BaseEvent):
    """Fake second emitted event."""


class FakeThirdEvent(BaseEvent):
    """Fake third emitted event."""


def test_event_history() -> None:
    """Test that event history is returned in expected order."""
    # Given: Event with two parent events
    first_event = FakeFirstEvent(parent_event=None)
    second_event = FakeSecondEvent(parent_event=first_event)
    third_event = FakeThirdEvent(parent_event=second_event)

    # When: get history is called on last *emitted* event
    # Then: parents are returned in the order of emittion
    #   (first returned is first chronologically emitted)
    assert third_event.get_history() == (first_event, second_event)
