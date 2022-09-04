
# Yet another event bus - yaeb for short

A simple typed event bus written in pure python


## Installation

Install yaeb with pip

```bash
  pip install yaeb
```
    
## Usage/Examples

```python
from logging import info

from yaeb.base.bus import BaseEventBus
from yaeb.base.events import BaseEvent
from yaeb.base.handlers import BaseSyncEventHandler
from yaeb.bus import DictEventHandlerRegistry, EventBus


class UserCreated(BaseEvent):
    user_id: int

    def __init__(self, user_id: int) -> None:
        self.user_id = user_id


class UserCreatedHandler(BaseSyncEventHandler[UserCreated]):
    def handle_event(self, event: UserCreated, bus: BaseEventBus) -> None:
        info('User with id=%d was created!', event.user_id)


if __name__ == '__main__':
    bus = EventBus(event_handler_registry=DictEventHandlerRegistry())
    bus.register(event_type=UserCreated, event_handler=UserCreatedHandler())

    bus.emit(UserCreated(user_id=1))  # prints log message with created user id

```


## Roadmap

- [x] Add coroutines support - Added `BaseAsyncEventHandler`
- [x] Add some kind of multithreading support. Though it can be implemented by handlers themselves 🤔 - Added `BaseExecutorEventHandler`

