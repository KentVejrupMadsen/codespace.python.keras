from random \
    import SystemRandom

from sys \
    import maxsize

max_seed_value = maxsize - 2
min_seed_value = 0


def get_maximum_seed_value() -> int:
    global max_seed_value
    return max_seed_value


def get_minimum_seed_value() -> int:
    global min_seed_value
    return min_seed_value


def generate_seed() -> int:
    randomizer = SystemRandom()

    return randomizer.randint(
        get_minimum_seed_value(),
        get_maximum_seed_value()
    )


