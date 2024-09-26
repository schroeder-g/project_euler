print(
    "\n".join(
        sorted(
            scorer[0] for scorer in list_of_grades if scorer[1] == sorted_score_set[1]
        )
    )
)
