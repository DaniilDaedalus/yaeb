"""Module containing event bus factories."""
import factory

from tests.factories.base import BaseFactory
from tests.factories.registry import DictEventHandlerRegistryFactory
from yaeb.bus import EventBus


class EventBusFactory(BaseFactory[EventBus]):
    """Event bus factory."""

    class Meta:
        """Event bus factory config."""

        model = EventBus

    event_handler_registry = factory.SubFactory(DictEventHandlerRegistryFactory)
