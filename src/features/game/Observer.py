from abc import ABC, abstractmethod
from .Event import Event


class Observer(ABC):
    @abstractmethod
    def update(self, event: Event) -> None:
        """Receive an update about a game event."""
        pass
