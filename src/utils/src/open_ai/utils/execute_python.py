import ast


def python(code: str):
    "Return result of executing `code` using python. If execution not permitted, returns `#FAIL#`"
    go = input(f"\nProceed with execution?\n```\n{code}\n```\n")
    if go.lower() != "y":
        return "#FAIL#"
    return run(code)


def run(code):
    "Execute `code` and return the result"
    tree = ast.parse(code)
    last_node = tree.body[-1] if tree.body else None

    # If the last node is an expression, modify the AST to capture the result
    if isinstance(last_node, ast.Expr):
        tgts = [ast.Name(id="_result", ctx=ast.Store())]
        assign = ast.Assign(targets=tgts, value=last_node.value)
        tree.body[-1] = ast.fix_missing_locations(assign)

    ns = {}
    exec(compile(tree, filename="<ast>", mode="exec"), ns)
    return ns.get("_result", None)
