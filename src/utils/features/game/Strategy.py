from abc import ABC, abstractmethod
from typing import Any

from .GameState import GameState
from .Action import Action


class Strategy(ABC):
    @abstractmethod
    def decide_action(self, game_state: GameState, player_state: Any) -> Action:
        """Determine the next action based on the game and player state."""
        pass
