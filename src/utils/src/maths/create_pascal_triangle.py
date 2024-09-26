def create_pascal_triangle(n, ans=None):
    if not ans:
        ans = []

    if n == 1:
        ans.append([1])
    else:
        ans.extend(create_pascal_triangle(n - 1, ans))
        curr = []
        for i in range(0, n):
            if i == 0 or i == n - 1:
                curr.append(1)
            else:
                curr.append(ans[n - 2][i - 1] + ans[n - 2][i])
        ans.append(curr)
    return ans
