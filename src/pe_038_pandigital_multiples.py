from project_euler.utils.read_out_file import read_out_file

# https://projecteuler.net/problem=38


class PandigitalMultipleGenerator:

    def __init__(self):
        self.perms = read_out_file(
            "permutations_1_to_9"
        )  # All possible permutations of the digits 1 - 9

        self.pandigit = None  # The number we are checking
        # The possible multiple base for this pandigital
        self.root_divisor: int = None

        self.k = 4  # The end delimiter of our current multiple
        self.n = 1  # The current multiple of our base (root_divisor)

    @property
    def next_multiple(self):
        return self.root_divisor * (self.n + 1) if self.root_divisor else -1

    @property
    def root_candidate(self):
        return int(self.pandigit[: self.k])

    def increment_k(self):
        self.k += 1

    def show_status(self):
        print(
            f"""
        n: {self.n} k: {self.k}

        root: {self.root_divisor}
        candidate: {self.root_candidate}
        next: {self.next_multiple}

        """
        )

    def is_succeeded_by_multiple(self, v, m=2) -> bool:
        return self.pandigit[self.k :].startswith(str(v * m))

    def generate(self):

        for pandigit in reversed(self.perms):
            if len(pandigit) < 9:
                continue

            # print(f"""\n\nchecking: {pandigit}\n- - - - - - - - - -\n""")
            self.pandigit = pandigit

            while self.k <= len(pandigit) // 2 + 1:
                # self.show_status()

                if self.root_divisor is None:
                    if self.is_succeeded_by_multiple(self.root_candidate):
                        self.root_divisor = int(self.root_candidate)
                        print(f"root set: {self.root_divisor}")

                        root_product = str(self.root_divisor)

                        while len(root_product) < len(self.pandigit):
                            root_product += str(self.next_multiple)
                            self.n += 1

                            if root_product == self.pandigit:
                                yield self.pandigit
                                break
                        break
                    else:
                        # noqa: E501 print(f'Searching for root. Incremented k to {self.k}\n____________________\n')
                        self.increment_k()

            self.__init__()


def generate_pandigital_products():
    generator = PandigitalMultipleGenerator().generate()

    pandigital_multiples = []
    for product in generator:
        print(
            f"""
        ****************************************
        ***     pan dig found: {product}     ***
        ****************************************
        """
        )
        pandigital_multiples.append(product)

    print(pandigital_multiples)


# generate_pandigital_products()

result = 0
for a in range(1, 10000):
    temporary = ""
    for b in range(1, 5):
        temporary += str(a * b)
        if sorted(temporary) == list("123456789"):
            result = temporary
        if len(temporary) > 9:
            break


print(result)
