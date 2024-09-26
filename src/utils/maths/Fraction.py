from dataclasses import dataclass
from fractions import Fraction


@dataclass
class Frac47:
    numerator: int | float
    denominator: int | float

    @property
    def fraction(self):
        return Fraction(self.numerator, self.denominator)

    def get_reductions(self) -> list[tuple]:
        reductions = []
        common_factors = filter(
            lambda n: n != 0, get_common_factors(self.numerator, self.denominator)
        )

        for common in common_factors:
            reductions.append((self.numerator // common, self.denominator // common))

        return reductions

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
