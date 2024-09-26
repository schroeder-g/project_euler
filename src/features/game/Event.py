from typing import Any, Dict
from abc import ABC, abstractmethod

from .GameState import GameState


class Event(ABC):
    @property
    @abstractmethod
    def event_type(self) -> str:
        pass

    @property
    @abstractmethod
    def event_data(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def process(self, game_state: GameState) -> None:
        """Process the event and update the game state."""
        pass
