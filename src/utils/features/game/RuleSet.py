from abc import ABC, abstractmethod
from typing import List, Optional

from .Action import Action
from .GameState import GameState
from .Player import Player


class RuleSet(ABC):
    @property
    @abstractmethod
    def game_name(self) -> str:
        pass

    @abstractmethod
    def validate_action(
        self, game_state: GameState, player: Player, action: Action
    ) -> bool:
        """Check if the action is valid according to the game rules."""
        pass

    @abstractmethod
    def apply_action(
        self, game_state: GameState, player: Player, action: Action
    ) -> None:
        """Update the game state based on the action."""
        pass

    @abstractmethod
    def get_initial_state(self) -> GameState:
        """Return the initial game state."""
        pass

    @abstractmethod
    def evaluate_game_state(self, game_state: GameState) -> Optional[Player]:
        """Determine if the game has ended and identify the winner."""
        pass

    @abstractmethod
    def get_possible_actions(
        self, game_state: GameState, player: Player
    ) -> List[Action]:
        """Get possible actions for the player."""
        pass
