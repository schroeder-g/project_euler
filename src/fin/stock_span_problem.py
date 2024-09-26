def stock_span(prices):
    # Initialize our answer array and a stack for solving subproblems
    n = len(prices)
    spans, prev_prices = [1 for _ in range(n)], [0]

    for i in range(1, n):
        while len(prev_prices) > 0 and prices[prev_prices[-1]] <= prices[i]:
            prev_prices.pop()

        spans[i] = i + 1 if len(prev_prices) <= 0 else i - prev_prices[-1]
        prev_prices.append(i)
    return spans


price_test = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(price_test))
