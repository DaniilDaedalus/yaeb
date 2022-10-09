"""Module containing registry factories."""
from tests.factories.base import BaseFactory
from yaeb.bus import DictEventHandlerRegistry


class DictEventHandlerRegistryFactory(BaseFactory[DictEventHandlerRegistry]):
    """Dict event handler registry factory."""

    class Meta:
        """Dict event handler registry factory config."""

        model = DictEventHandlerRegistry
