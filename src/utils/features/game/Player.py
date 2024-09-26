from abc import ABC, abstractmethod
from typing import Any

from .GameState import GameState
from .Action import Action


class Player(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def decide_action(self, game_state: GameState) -> Action:
        """Decide the next action based on the game state."""
        pass

    @abstractmethod
    def update_player_state(self, game_state: GameState) -> None:
        """Update internal player state."""
        pass

    @abstractmethod
    def reset(self) -> None:
        """Reset the player's state for a new game."""
        pass

    @abstractmethod
    def notify(self, event: Any) -> None:
        """Receive notifications from the game."""
        pass
