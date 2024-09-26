# from out.read_out_file import read_out_file
from dataclasses import dataclass
from features.game.GameState import GameState


@dataclass(frozen=True)
class Card:
    value: str
    suit: str

    @staticmethod
    def from_DTO(raw: str):
        return Card(suit=raw[-1], value=raw[:-1])

    def __str__(self):
        face_map = {"K": "King", "J": "Jack", "Q": "Queen", "A": "Ace"}
        suit_map = {"S": "Spades", "H": "Hearts", "D": "Diamonds", "C": "Clubs"}

        value = self.value if self.value.isnumeric() else face_map[self.value]
        suit = suit_map[self.suit]

        return f"{value} of {suit}"


class PokerHand:
    def __init__(self, cards: str):
        self.cards: [Card] = PokerHand.sanitize_hand(cards)

    @staticmethod
    def sanitize_hand(cards: [str]):
        return [Card.from_DTO(c) for c in cards]

    def __str__(self):
        return ", ".join(str(c) for c in self.cards)


class PokerGame(GameState):
    @staticmethod
    def compare_hands():
        pass

    # GameState.sanitize_hands(read_out_file('poker_hands', True))
    # @staticmethod
    # def sanitize_hands(hand_pairs: list):
    # noqa: E501    return list(map(lambda hs: (PokerHand(hs[:5]), PokerHand(hs[5:])), [pair.split(' ') for pair in hand_pairs]))


# https://projecteuler.net/problem=54

# muff = StudMuffin()

print(PokerHand(cards=["AS", "10D"]))
