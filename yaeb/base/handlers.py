"""Module storing base event bus handlers."""
from __future__ import annotations

import abc
import asyncio
from typing import TYPE_CHECKING, Generic, TypeVar

from yaeb.base.events import BaseEvent

if TYPE_CHECKING:
    from concurrent.futures import Executor

    from yaeb.base.bus import BaseEventBus

E = TypeVar('E', bound=BaseEvent)


class BaseEventHandler(abc.ABC, Generic[E]):
    """Base class for event handlers."""

    @abc.abstractmethod
    def execute(self, event: E, bus: BaseEventBus) -> None:
        """Execute handling of event."""
        raise NotImplementedError


class BaseAsyncEventHandler(BaseEventHandler[E]):
    """Base class for async event handlers."""

    @abc.abstractmethod
    async def handle_event(self, event: E, bus: BaseEventBus) -> None:
        """Handle given event asynchronously."""
        raise NotImplementedError

    def execute(self, event: E, bus: BaseEventBus) -> None:
        """Execute event handling via asyncio task asynchronously."""
        asyncio.Task(self.handle_event(event=event, bus=bus))


class BaseSyncEventHandler(BaseEventHandler[E]):
    """Base class for sync event handlers."""

    @abc.abstractmethod
    def handle_event(self, event: E, bus: BaseEventBus) -> None:
        """Handle given event synchronously."""
        raise NotImplementedError

    def execute(self, event: E, bus: BaseEventBus) -> None:
        """Execute handling of event simply by calling handle event method."""
        self.handle_event(event=event, bus=bus)


class BaseExecutorEventHandler(BaseEventHandler[E]):
    """Base event handler handling events via given executor."""

    executor: Executor

    def __init__(self, executor: Executor) -> None:
        """Add executor for further handle event execution."""
        self.executor = executor

    @abc.abstractmethod
    def handle_event(self, event: E, bus: BaseEventBus) -> None:
        """Handle event in the given executor."""
        raise NotImplementedError

    def execute(self, event: E, bus: BaseEventBus) -> None:
        """Pass handle event to given executor."""
        self.executor.submit(self.handle_event, event=event, bus=bus)
