from dataclasses import dataclass, astuple


@dataclass
class MovingWindow:
    start: int
    end: int

    def get(self):
        return astuple(self)

    def decrement(self):
        self.start -= 1
        self.end -= 1

    def increment(self):
        self.start += 1
        self.end += 1
