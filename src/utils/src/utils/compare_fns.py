import timeit


def compare_dos_funcs(f1, f2, d):
    t1, t2 = timeit.timeit(lambda: f1(d), number=2500), timeit.timeit(
        lambda: f2(d), number=100000
    )
    print(
        f"It took f1 {round(t1, 3)} seconds and f2 {round(t2, 3)} seconds to complete 100000 repetitions. \n"
        f"{'f1' if t1 - t2 <= 0 else 'f2'} is approximately {round(abs(t1 - t2), 3)} seconds faster."
    )


if __name__ == "__main__":
    data = [
        ["Sam", 500],
        ["verv", 699],
        ["DaVinci", 600],
        ["Alex", 600],
        ["Homeboi", 500],
    ]

    def f1(gradebook):
        sorted_score_set = sorted(set([scorer[1] for scorer in gradebook]))
        print(
            "\n".join(
                sorted(
                    scorer[0]
                    for scorer in gradebook
                    if scorer[1] == sorted_score_set[1]
                )
            )
        )

    def f2(gradebook):
        print("hi")

    compare_dos_funcs(f1, f2, data)
