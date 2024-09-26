def buy_sell(prices):
    mapped_potential_returns = []
    greatest_potential_return = 0
    prev_low = {"val": 0, "index": -1}

    for i in range(0, len(prices), 1):
        current_val = prices[i]

        # check current val against lowest previous value.
        # If lowest previous value index is n/a, or is greater than
        # current val, set lowest val / index accordingly
        if current_val < prev_low["val"] or prev_low["index"] == -1:
            prev_low = {"val": current_val, "index": i}

        mapped_potential_returns.append(current_val - prev_low["val"])
        if mapped_potential_returns[i] > greatest_potential_return:
            greatest_potential_return = mapped_potential_returns[i]

    print("daily potential returns: ", mapped_potential_returns)
    return greatest_potential_return


prices = [0, 6, 5, 2, 3, 4, 7, 0]
print("greatest return: ", buy_sell(prices))
