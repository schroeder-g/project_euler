from abc import ABC, abstractmethod
from typing import List

from .Player import Player
from .RuleSet import RuleSet


class Game(ABC):
    def __init__(self, players: List[Player], ruleset: RuleSet):
        self.game_state = ruleset.get_initial_state()
        self.players = players
        self.ruleset = ruleset

    @abstractmethod
    def start(self) -> None:
        """Initialize the game."""
        pass

    @abstractmethod
    def play_turn(self) -> None:
        """Execute a single turn."""
        pass

    @abstractmethod
    def run(self) -> None:
        """Run the game loop."""
        pass

    @abstractmethod
    def end(self) -> None:
        """Finalize the game."""
        pass
