import random


def montecarlo():
    while True:
        r1 = random.random()
        probability = r1
        r2 = random.random()
        if r2 < probability:
            return r1


print(montecarlo())
