from maths.is_prime import is_prime
from maths import Fraction
from fractions import Fraction as Frac47
from functools import reduce


# https://projecteuler.net/problem=33
class FractionAnalyzer:
    def __init__(self):
        self.fraction: Frac47 = None

    @property
    def numerator(self):
        return self.fraction.numerator

    @property
    def denominator(self):
        return self.fraction.denominator

    def _set(self, numerator: int, denominator: int):
        self.fraction = Frac47(numerator=numerator, denominator=denominator)

    def generate_range(self):
        for denominator in range(11, 100, 1):
            for numerator in range(11, denominator, 1):
                self._set(numerator=numerator, denominator=denominator)
                yield self.fraction

    def is_cancellable_fraction(self):
        d = self.denominator
        n = self.numerator

        def has_mirrored_digits():
            return any([True if char in str(n) else False for char in str(d)])

        def is_trivial():
            return n % 10 == 0 and d % 10 == 0 or n % 11 == 0

        evaluation = (
            False
            if any([is_prime(d), is_trivial()])
            else True if has_mirrored_digits() else False
        )

        return evaluation

    def denominatorduct_of_cancellable_fraction_product(self):
        ret = []

        for frac in self.generate_range():
            if self.is_cancellable_fraction():

                def does_cancelled_digit_reduce():
                    def get_cancelled_frac(d: str):
                        def cancel(n):
                            cancelled = "".join(filter(lambda c: c != d, str(n)))
                            return int(cancelled) if cancelled else int(d)

                        new_numerator = cancel(self.numerator)
                        new_denominator = cancel(self.denominator)

                        return Frac47(
                            numerator=new_numerator, denominator=new_denominator
                        )

                    for char in str(self.denominator):
                        cancelled_frac_obj = get_cancelled_frac(char)
                        new_denominator = cancelled_frac_obj.denominator

                        if new_denominator == 0:
                            continue

                        try:
                            cancelled_fraction = Fraction(
                                cancelled_frac_obj.numerator,
                                cancelled_frac_obj.denominator,
                            )
                        except ZeroDivisionError:
                            continue

                        if cancelled_fraction == self.fraction.fraction:
                            return True

                    return False

                if does_cancelled_digit_reduce():
                    ret.append(frac)

        return reduce(lambda acc, curr: acc * curr.fraction, ret, Fraction(1, 1))


f = FractionAnalyzer()
print(f.get_denominator_of_cancellable_fraction_product())
