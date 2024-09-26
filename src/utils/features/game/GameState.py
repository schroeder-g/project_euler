from abc import ABC, abstractmethod
from typing import List, Optional
from .Player import Player
from .Action import Action


class GameState(ABC):
    @property
    @abstractmethod
    def players(self) -> List[Player]:
        pass

    @property
    @abstractmethod
    def current_turn(self) -> Player:
        pass

    @property
    @abstractmethod
    def game_phase(self) -> str:
        pass

    @abstractmethod
    def update_state(self, action: Action) -> None:
        """Update the game state based on the action taken."""
        pass

    @abstractmethod
    def get_valid_actions(self, player: Player) -> List[Action]:
        """Return valid actions for the given player."""
        pass

    @abstractmethod
    def is_game_over(self) -> bool:
        """Check if the game has ended."""
        pass

    @abstractmethod
    @Optional
    def get_winner(self) -> Optional[Player]:
        """Identify the winner(s) of the game."""
        pass

    @abstractmethod
    def clone(self) -> "GameState":
        """Create a deep copy of the game state."""
        pass
