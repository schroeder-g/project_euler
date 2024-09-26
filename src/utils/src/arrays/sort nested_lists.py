def sort_by_score(list_of_grades):
    second_highest = sorted(set([scorer[1] for scorer in list_of_grades]))[1]
    print(
        "\n".join(
            sorted(
                scorer[0] for scorer in list_of_grades if scorer[1] == second_highest
            )
        )
    )


if __name__ == "__main__":
    sort_by_score([[input(), float(input())] for _ in range(0, int(input()))])
